# Suno Prompt Suffix (CCat Plugin)

Cheshire Cat AI plugin to help create optimized prompts for Suno AI.

## Dynamic System
This plugin uses a **dynamic file-to-command system**.
- Any Markdown file placed in the `documents/` folder automatically becomes a command.
- **Example**: `documents/my_guide.md` -> Trigger `:my_guide:`

## Educational Notes
This plugin is designed to be a learning resource for Cheshire Cat development:
- **Hooks**: See `plugin.py` to understand how `before_cat_reads_message` intercepts prompts.
- **Settings**: See `settings.py` for Pydantic-based configuration.
- **Dynamic Loading**: The plugin scans the file system to create commands on the fly.
- **Token Counting**: Uses `tiktoken` (cl100k_base) to estimate token usage for injected content.

## Default Commands
- `:s1:` (from `documents/s1.md`): **Metrics & Lyrics Guide**.
- `:s2:` (from `documents/s2.md`): **Suno Formatting Guide**.

## Configuration
- **commands.json**: Automatically generated. Edit this file to customize triggers, instructions, and wrapper templates for each document.
- **Settings**:
    - **Educational Mode**: Toggles chat instructions.
    - **Auto Reload**: Toggles automatic scanning of new files.

## Installation
1. Copy the `suno-suffix` folder to your Cheshire Cat's `cat/plugins/` folder.
2. Restart the Cat.

## Acknowledgments
Special thanks to the **Cheshire Cat AI** team for creating such an amazing and extensible framework.
- [Cheshire Cat AI Website](https://cheshirecat.ai/)
- [GitHub Repository](https://github.com/cheshire-cat-ai/core)
