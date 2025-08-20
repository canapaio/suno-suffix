import os
from cat.mad_hatter.decorators import hook
from cat.log import log

def find_guida_file(filename, folder_hint, plugin_path):
    """Cerca il file guida in varie posizioni"""
    search_paths = []
    
    # 1. Cartella specificata (se non vuota)
    if folder_hint:
        search_paths.append(os.path.join(folder_hint, filename))
    
    # 2. Cartella del plugin
    search_paths.append(os.path.join(plugin_path, filename))
    
    # 3. Cartella parent del plugin
    search_paths.append(os.path.join(os.path.dirname(plugin_path), filename))
    
    # 4. Cartella plugins generale
    plugins_dir = os.path.dirname(plugin_path)
    search_paths.append(os.path.join(plugins_dir, filename))
    
    for path in search_paths:
        if os.path.exists(path):
            log.info(f"Guida Suno trovata: {path}")
            return path
    
    log.warning(f"Guida Suno non trovata. Cercato in: {search_paths}")
    return None

@hook
def agent_prompt_suffix(suffix, cat):
    # Carica le impostazioni dal Cat
    settings = cat.mad_hatter.get_plugin_settings()
    
    # Ottieni il messaggio dell'utente
    user_message = cat.working_memory.user_message_json.text
    
    # Controlla se il trigger è presente
    trigger = settings.get('trigger', ':s:')
    if trigger in user_message:
        log.info(f"🎵 Trigger '{trigger}' rilevato! Aggiungendo guida Suno...")
        
        # Cerca il file della guida
        guida_filename = settings.get('guida_filename', 'mini_guida_suno_4.5.md')
        guida_folder = settings.get('guida_folder', '')
        guida_path = find_guida_file(guida_filename, guida_folder, cat.mad_hatter.find_plugin(__file__))
        
        if guida_path:
            try:
                with open(guida_path, 'r', encoding='utf-8') as f:
                    guida_content = f.read()
                log.info(f"📖 Guida Suno caricata da: {guida_path}")
                return suffix + "\n\n" + guida_content
            except Exception as e:
                log.error(f"❌ Errore lettura guida: {e}")
                return suffix + "\n\n[Errore: impossibile leggere la guida Suno]"
        else:
            log.warning(f"⚠️ File guida '{guida_filename}' non trovato")
            return suffix + "\n\n[Guida Suno non disponibile]"
    
    return suffix