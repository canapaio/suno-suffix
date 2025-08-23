import os
from cat.mad_hatter.decorators import hook
from cat.log import log

def apply_trigger_substitution(text, settings, cat):
    """Centralized function to handle trigger substitution"""
    trigger = settings.get('trigger', ':s:')
    
    if trigger in text:
        log.info(f"Trigger '{trigger}' detected. Processing substitution.")
        
        # Mark that trigger was detected
        cat.working_memory.suno_trigger_detected = True
        
        # Get phase instructions from settings
        if settings.get('auto_add_instructions', True):
            phase_instructions = settings.get('phase_instructions', 
                'Segui rigorosamente le fasi A→B→C→D della guida in sequenza. Inizia sempre con una strategia chiara, poi procedi con FASE A (GENERE), FASE B (STYLE), FASE C (TEMPO E METRICA), FASE D (FINAL TEXT). Mantieni coerenza tra tutte le fasi.')
            
            # Replace trigger with instructions in parentheses
            instructions_with_parentheses = f"({phase_instructions})"
            return text.replace(trigger, instructions_with_parentheses)
        else:
            # Just remove trigger if instructions are disabled
            return text.replace(trigger, '').strip()
    else:
        # Reset trigger detection if not present
        cat.working_memory.suno_trigger_detected = False
        return text

@hook
def before_cat_reads_message(user_message_json, cat):
    """Hook to intercept and modify user messages before LLM processing"""
    # Load plugin settings
    settings = cat.mad_hatter.get_plugin().load_settings()
    
    # Apply trigger substitution only if save_in_history is True
    if settings.get('save_in_history', True):
        user_message_json.text = apply_trigger_substitution(user_message_json.text, settings, cat)
    else:
        # Just check for trigger presence without substitution
        trigger = settings.get('trigger', ':s:')
        if trigger in user_message_json.text:
            cat.working_memory.suno_trigger_detected = True
        else:
            cat.working_memory.suno_trigger_detected = False
    
    return user_message_json

def find_guide_file(filename, folder_hint, plugin_path):
    """Search for the guide file in various locations"""
    search_paths = []
    
    # 1. Specified folder (if not empty)
    if folder_hint:
        search_paths.append(os.path.join(folder_hint, filename))
    
    # 2. Plugin directory
    search_paths.append(os.path.join(plugin_path, filename))
    
    # 3. Parent directory of plugin
    search_paths.append(os.path.join(os.path.dirname(plugin_path), filename))
    
    # 4. General plugins directory
    plugins_dir = os.path.dirname(plugin_path)
    search_paths.append(os.path.join(plugins_dir, filename))
    
    for path in search_paths:
        if os.path.exists(path):
            log.info(f"Guide file found: {path}")
            return path
    
    log.warning(f"Guide file not found. Searched in: {search_paths}")
    return None

@hook
def agent_prompt_suffix(suffix, cat):
    # Load plugin settings
    settings = cat.mad_hatter.get_plugin().load_settings()
    
    # Get user message
    user_message = cat.working_memory.user_message_json.text
    trigger = settings.get('trigger', ':s:')
    
    # Apply trigger substitution if save_in_history is False
    if not settings.get('save_in_history', True):
        if trigger in user_message:
            # Apply substitution to the message in working memory
            cat.working_memory.user_message_json.text = apply_trigger_substitution(user_message, settings, cat)
    
    # Check if trigger was detected (either by before_cat_reads_message or here)
    trigger_detected = hasattr(cat.working_memory, 'suno_trigger_detected') and cat.working_memory.suno_trigger_detected
    
    # Also check current message for backward compatibility
    if trigger in user_message:
        trigger_detected = True
        cat.working_memory.suno_trigger_detected = True
    
    if trigger_detected:
        log.info(f"Trigger '{trigger}' detected. Loading guide content...")
        
        # Search for the guide file
        guide_filename = settings.get('guide_filename', 'guida_sunoV4.md')
        guide_folder = settings.get('guide_folder', '')
        plugin_dir = os.path.dirname(__file__)
        guide_path = find_guide_file(guide_filename, guide_folder, plugin_dir)
        
        content_parts = []
        
        # Add guide content (instructions are now injected directly in the user message)
        if guide_path:
            try:
                with open(guide_path, 'r', encoding='utf-8') as f:
                    guide_content = f.read()
                log.info(f"Guide content loaded from: {guide_path}")
                # Wrap guide content using configurable template
                guide_template = settings.get('guide_wrapper_template', 
                    '<guida_tecnica format="markdown" type="suno_advanced">\n{guide_content}\n</guida_tecnica>')
                wrapped_content = guide_template.format(guide_content=guide_content)
                content_parts.append(wrapped_content)
            except Exception as e:
                log.error(f"Error reading guide file: {e}")
                content_parts.append("[Error: Unable to read guide file]")
        else:
            log.warning(f"Guide file '{guide_filename}' not found")
            content_parts.append("[Guide content not available]")
        
        if content_parts:
            return suffix + "\n\n" + "\n\n".join(content_parts)
    
    return suffix
