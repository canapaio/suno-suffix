from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field

class SunoSettings(BaseModel):
    """
    Settings configuration for the Suno Plugin.
    
    This class defines the options available in the Cheshire Cat's admin panel.
    It uses Pydantic for data validation and type checking.
    """
    
    # === GLOBAL SETTINGS ===
    educational_mode: bool = Field(
        default=True,
        description="Educational Mode: Shows detailed instructions in chat when a trigger is detected. Useful for learning how prompts are constructed."
    )
    
    auto_reload_config: bool = Field(
        default=True,
        description="Smart Reload: Automatically checks if document files have changed on every message. If changed, it reloads the configuration and updates token counts. (Optimized for performance)"
    )

    documents_path: str = Field(
        default="",
        description="Absolute path to the documents folder. The plugin attempts to auto-detect this on startup using the 'suno_plugin_marker.txt' file."
    )

    save_in_history: bool = Field(
        default=True,
        description="Save modified prompt (with injected content) in chat history. If disabled, the injection happens 'silently' before the LLM sees it, but isn't saved in the user's chat log."
    )

    commands_json: str = Field(
        default="{}",
        description="Edit the commands.json configuration directly. WARNING: Invalid JSON will be ignored.",
        json_schema_extra={"type": "textarea"}
    )

@plugin
def settings_model():
    """
    Register the settings model with the Cheshire Cat.
    This function is called by the Cat to know which settings to display.
    """
    return SunoSettings
