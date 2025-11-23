import os
import json
import tiktoken
from cat.mad_hatter.decorators import hook
from cat.log import log

# Constants for file paths
PLUGIN_DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(PLUGIN_DIR, "commands.json")

def get_documents_path(settings):
    """
    Determine the absolute path to the 'documents' folder.
    
    This function implements a robust discovery strategy:
    1. Checks if a path is already saved in the settings.
    2. Checks if the 'documents' folder exists relative to this script.
    3. Searches recursively for a unique marker file ('suno_plugin_marker.txt') to find the plugin root.
    
    Returns:
        str: The absolute path to the documents folder, or empty string if not found.
    """
    # 1. Check settings
    doc_path = settings.get("documents_path", "")
    if doc_path and os.path.exists(doc_path):
        return doc_path
    
    # 2. Check relative to this file (fastest)
    base_dir = os.path.dirname(__file__)
    potential_path = os.path.join(base_dir, "documents")
    if os.path.exists(potential_path):
        return potential_path
        
    # 3. Search for marker file (robust)
    # This handles cases where the plugin might be symlinked or in a nested structure
    log.warning("Suno Plugin: Documents path not found. Searching for marker file...")
    marker_file = "suno_plugin_marker.txt"
    
    # Search in current directory and subdirectories (assuming we are in cat root)
    root_search = os.getcwd()
    for root, dirs, files in os.walk(root_search):
        if marker_file in files:
            found_dir = root
            doc_path = os.path.join(found_dir, "documents")
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            log.info(f"Suno Plugin: Marker found at {found_dir}. Setting documents path to {doc_path}")
            return doc_path
            
    return ""

def load_config():
    """
    Load the JSON configuration from disk.
    
    Returns:
        dict: The configuration dictionary, or empty if file doesn't exist/fails to load.
    """
    if not os.path.exists(CONFIG_FILE):
        return {}
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        log.error(f"Error loading commands.json: {e}")
        return {}

def save_config(config):
    """
    Save the configuration dictionary to disk as JSON.
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except Exception as e:
        log.error(f"Error saving commands.json: {e}")

def calculate_stats(content):
    """
    Calculate text statistics using the 'cl100k_base' tokenizer.
    
    This tokenizer is used by OpenAI's GPT-4, GPT-3.5-turbo, and also by models like Qwen and Llama 3.
    It provides a standard way to estimate token usage.
    
    Args:
        content (str): The text content to analyze.
        
    Returns:
        dict: A dictionary containing 'chars' (int) and 'tokens' (int).
    """
    char_count = len(content)
    try:
        encoding = tiktoken.get_encoding("cl100k_base") # GPT-4/3.5 encoding
        token_count = len(encoding.encode(content))
    except Exception as e:
        log.error(f"Suno Plugin: Error calculating tokens: {e}")
        token_count = 0
    return {"chars": char_count, "tokens": token_count}

def needs_update(docs_dir, current_config):
    """
    Check if any document has been modified since the last configuration save.
    
    This is a performance optimization ("Smart Reload"). Instead of reading and tokenizing
    every file on every message, we just check the file modification time (mtime).
    
    Returns:
        bool: True if an update is needed, False otherwise.
    """
    # Check if config is empty but files exist
    if not current_config and os.path.exists(docs_dir) and os.listdir(docs_dir):
        return True
        
    # Get last config update time (approximate via file mtime of the json file)
    config_mtime = 0
    if os.path.exists(CONFIG_FILE):
        config_mtime = os.path.getmtime(CONFIG_FILE)
        
    # Check documents
    if os.path.exists(docs_dir):
        for f in os.listdir(docs_dir):
            if f.endswith('.md'):
                file_path = os.path.join(docs_dir, f)
                # If file is newer than config, we need to update
                if os.path.getmtime(file_path) > config_mtime:
                    log.info(f"Suno Plugin: Detected change in {f}. Triggering update.")
                    return True
                    
    return False

def generate_instruction(content, cat):
    """
    Generate a short instruction for a document using the LLM.
    
    Args:
        content (str): The content of the document.
        cat (CheshireCat): The Cat instance.
        
    Returns:
        str: A short instruction string.
    """
    try:
        prompt = f"""Analyze the following document content and write a very short, one-sentence instruction for an AI on how to use it.
        Example: "Use this guide to format lyrics according to Suno specifications."
        
        Document Content:
        {content[:2000]} # Truncate to avoid huge prompts
        
        Instruction:"""
        
        # Use the Cat's LLM to generate the instruction
        # We use a direct call if possible, or a simple predict
        instruction = cat.llm.predict(prompt)
        return instruction.strip()
    except Exception as e:
        log.error(f"Suno Plugin: Error generating instruction: {e}")
        return "(Injecting content from document)"

def scan_documents(current_config, settings, cat=None, force=False):
    """
    Scan the documents folder and update the configuration.
    
    This function:
    1. Finds all .md files in the documents folder.
    2. Checks if the file is already registered in the config.
    3. If NEW, assigns a progressive trigger (e.g., :s3:, :s4:) based on available slots.
    4. Calculates token/char stats.
    5. Updates 'commands.json' if anything is new or changed.
    6. If a new file is found and 'cat' is provided, generates an instruction via LLM.
    
    Args:
        current_config (dict): The current loaded configuration.
        settings (dict): Plugin settings.
        cat (CheshireCat): The Cat instance (optional, needed for LLM generation).
        force (bool): If True, forces a scan even if timestamps haven't changed.
    """
    docs_dir = get_documents_path(settings)
    
    if not docs_dir or not os.path.exists(docs_dir):
        log.warning(f"Suno Plugin: Documents directory not found: {docs_dir}")
        return current_config

    # Smart Reload Check
    if not force and not needs_update(docs_dir, current_config):
        return current_config

    files = [f for f in os.listdir(docs_dir) if f.endswith('.md')]
    updated = False
    
    # Create a reverse mapping: filename -> command_key
    # This helps us quickly check if a file is already registered under ANY key
    filename_to_key = {}
    for key, data in current_config.items():
        if "filename" in data:
            filename_to_key[data["filename"]] = key
            
    for filename in files:
        file_path = os.path.join(docs_dir, filename)
        
        # Read content for stats
        content = ""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            log.error(f"Suno Plugin: Error reading {filename} for stats: {e}")
            continue
            
        stats = calculate_stats(content)
        
        if filename in filename_to_key:
            # Existing file: Update stats if needed
            key = filename_to_key[filename]
            if current_config[key].get("stats") != stats:
                current_config[key]["stats"] = stats
                updated = True
                log.info(f"Updated stats for {filename} (Key: {key}, Tokens: {stats['tokens']})")
        else:
            # New file found! Assign a progressive trigger.
            log.info(f"Suno Plugin: New document found: {filename}")
            
            # Find the next available 'sN' key
            used_indices = []
            for k in current_config:
                # Check for keys like 's1', 's2', 's10'
                if k.startswith('s') and k[1:].isdigit():
                    used_indices.append(int(k[1:]))
            
            next_index = 1
            while next_index in used_indices:
                next_index += 1
            
            command_name = f"s{next_index}"
            trigger = f":{command_name}:"
            
            # Generate instruction if Cat is available
            instruction = f"(Injecting content from {filename})"
            if cat:
                log.info(f"Suno Plugin: Generating auto-instruction for {filename}...")
                instruction = generate_instruction(content, cat)
                log.info(f"Suno Plugin: Generated instruction: {instruction}")
            
            current_config[command_name] = {
                "trigger": trigger,
                "filename": filename,
                "active": True,
                "instructions": instruction,
                "wrapper_template": f"<guide type=\"{command_name}\">\n{{content}}\n</guide>",
                "stats": stats
            }
            updated = True
            log.info(f"Registered new document: {filename} -> Key: {command_name}, Trigger: {trigger}")
            
    if updated:
        save_config(current_config)
        
    return current_config

@hook
def after_cat_bootstrap(cat):
    """
    Hook called when the Cheshire Cat starts up.
    
    We use this to:
    1. Auto-detect the documents path.
    2. Perform an initial scan of all documents to ensure the config is fresh.
    """
    settings = cat.mad_hatter.get_plugin().load_settings()
    
    # 1. Path Detection
    if not settings.get("documents_path"):
        detected_path = get_documents_path(settings)
        if detected_path:
            log.info(f"Suno Plugin: Auto-configuring documents path: {detected_path}")
            settings["documents_path"] = detected_path
            cat.mad_hatter.get_plugin().save_settings(settings)
    
    # 2. Initial Scan (Force update on startup to ensure consistency)
    log.info("Suno Plugin: Performing initial document scan...")
    # 2. Initial Scan (Force update on startup to ensure consistency)
    log.info("Suno Plugin: Performing initial document scan...")
    current_config = load_config()
    # Pass 'cat' to allow instruction generation for new files found at startup
    scan_documents(current_config, settings, cat=cat, force=True)

    # 3. Sync JSON to Settings (for UI editor)
    # We load the fresh config (after scan) into the settings field
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            settings["commands_json"] = content
            cat.mad_hatter.get_plugin().save_settings(settings)
    except Exception as e:
        log.error(f"Suno Plugin: Error syncing config to settings: {e}")

@hook
def after_plugin_settings_update(settings, cat):
    """
    Hook called when plugin settings are updated in the UI.
    
    We use this to sync the 'commands_json' field back to the file.
    """
    # Check if this is our plugin
    # Note: The hook might be generic, so we should be careful. 
    # But usually it passes the specific settings dict.
    
    if "commands_json" in settings:
        json_content = settings["commands_json"]
        try:
            # Validate JSON
            new_config = json.loads(json_content)
            
            # Save to file
            save_config(new_config)
            log.info("Suno Plugin: Updated commands.json from settings UI.")
            
        except json.JSONDecodeError:
            log.error("Suno Plugin: Invalid JSON in settings! Ignoring update.")
        except Exception as e:
            log.error(f"Suno Plugin: Error saving commands.json from settings: {e}")

@hook
def agent_prompt_suffix(suffix, cat):
    """
    Hook called to append text to the system prompt.
    
    We use this to inject document content ONLY for the LLM, keeping the
    vector memory (DB) clean. The user message in history will still contain
    the short triggers (e.g., :s1:), but the LLM will receive the full guides.
    """
    settings = cat.mad_hatter.get_plugin().load_settings()
    
    # Load config (Smart reload check happens inside scan_documents)
    config = load_config()
    if settings.get("auto_reload_config", True):
        # Pass 'cat' to allow instruction generation for new files found during reload
        config = scan_documents(config, settings, cat=cat)
        
    # Get the current user message
    # We need to check the working memory for the latest user message
    user_message = cat.working_memory.user_message_json
    if not user_message:
        return suffix
        
    user_text = user_message.text
    
    educational_mode = settings.get("educational_mode", True)
    docs_dir = get_documents_path(settings)
    
    injected_blocks = []
    
    # Check for triggers
    for cmd_name, cmd_data in config.items():
        if not cmd_data.get("active", True):
            continue
            
        trigger = cmd_data.get("trigger", f":{cmd_name}:")
        
        if trigger in user_text:
            log.info(f"Suno Plugin: Trigger {trigger} detected. Injecting content to prompt suffix.")
            
            # Load content
            file_path = os.path.join(docs_dir, cmd_data["filename"])
            content = ""
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    log.error(f"Error reading {file_path}: {e}")
                    content = f"[Error reading file: {cmd_data['filename']}]"
            else:
                content = f"[File not found: {cmd_data['filename']}]"
            
            # Format content
            wrapper = cmd_data.get("wrapper_template", "{content}")
            injected_content = wrapper.format(content=content)
            
            # Add instructions if educational mode is on
            if educational_mode:
                instr = cmd_data.get("instructions", "")
                if instr:
                    injected_blocks.append(f"--- INSTRUCTION FOR {trigger} ---\n{instr}")
            
            injected_blocks.append(f"--- DOCUMENT CONTENT FOR {trigger} ---\n{injected_content}")
            
    if injected_blocks:
        # Append all injected blocks to the suffix
        injection_text = "\n\n".join(injected_blocks)
        return f"{suffix}\n\n{injection_text}"
        
    return suffix
