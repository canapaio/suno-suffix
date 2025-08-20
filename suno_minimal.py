import os
from cat.mad_hatter.decorators import hook
from cat.log import log

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
    
    # Check if trigger is present
    trigger = settings.get('trigger', ':s:')
    if trigger in user_message:
        log.info(f"Trigger '{trigger}' detected. Loading guide content...")
        
        # Search for the guide file
        guide_filename = settings.get('guide_filename', 'mini_guida_suno_4.5.md')
        guide_folder = settings.get('guide_folder', '')
        plugin_dir = os.path.dirname(__file__)
        guide_path = find_guide_file(guide_filename, guide_folder, plugin_dir)
        
        if guide_path:
            try:
                with open(guide_path, 'r', encoding='utf-8') as f:
                    guide_content = f.read()
                log.info(f"Guide content loaded from: {guide_path}")
                return suffix + "\n\n" + guide_content
            except Exception as e:
                log.error(f"Error reading guide file: {e}")
                return suffix + "\n\n[Error: Unable to read guide file]"
        else:
            log.warning(f"Guide file '{guide_filename}' not found")
            return suffix + "\n\n[Guide content not available]"
    
    return suffix
