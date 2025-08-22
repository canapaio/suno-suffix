from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field

class SunoSettings(BaseModel):
    guide_filename: str = Field(
        default="guida_sunoV3.md",
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

@plugin
def settings_model():
    return SunoSettings
