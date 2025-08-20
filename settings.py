from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field

class SunoSettings(BaseModel):
    guida_filename: str = Field(
        default="mini_guida_suno_4.5.md",
        description="Nome del file della guida Suno"
    )
    guida_folder: str = Field(
        default="",
        description="Cartella custom per la guida (vuoto = ricerca automatica)"
    )
    trigger: str = Field(
        default=":s:",
        description="Trigger per attivare la guida Suno"
    )

@plugin
def settings_model():
    return SunoSettings