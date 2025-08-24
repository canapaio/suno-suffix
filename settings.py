from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field

class SunoSettings(BaseModel):
    guide_filename: str = Field(
        default="guida_sunoV4.5.md",
        description="Name of the guide file to load"
    )
    guide_folder: str = Field(
        default="",
        description="Custom folder for the guide file (empty = automatic search)"
    )
    trigger: str = Field(
        default=":s:",
        description="Trigger text to activate guide content injection"
    )
    auto_add_instructions: bool = Field(
        default=True,
        description="Automatically add phase instructions (A→B→C→D) when trigger is detected"
    )
    phase_instructions: str = Field(
        default="(Segui le fasi A→B→C→D→E della guida in sequenza. Inizia sempre con una strategia chiara, poi procedi con FASE A (PROGETTAZIONE), FASE B (CONFIGURATION), FASE C (STYLE), FASE D (TEMPO E METRICA), FASE E (FINAL TEXT). Mantieni coerenza tra tutte le fasi.)",
        description="Instructions to add when trigger is detected",
        extra={"type": "TextArea"}
    )
    guide_wrapper_template: str = Field(
        default="<guida_tecnica format=\"markdown\" type=\"suno_advanced\">\n{guide_content}\n</guida_tecnica>",
        description="Template for wrapping guide content. Use {guide_content} as placeholder for the actual guide text",
        extra={"type": "TextArea"}
    )
    save_in_history: bool = Field(
        default=True,
        description="If True, apply trigger substitution before saving to memory (before_cat_reads_message). If False, apply after saving to memory (agent_prompt_suffix)"
    )

@plugin
def settings_model():
    return SunoSettings
