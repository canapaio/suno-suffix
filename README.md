# Content Injection Plugin

**A versatile Cheshire Cat plugin that automatically injects guide content into prompts when triggered. While originally designed for Suno AI integration, this plugin can be adapted for any content injection use case.**

## 🚀 What it does

This plugin automatically adds comprehensive guide content to your prompt whenever you include a configurable trigger in your message. Perfect for injecting documentation, instructions, examples, or any reference material into your AI conversations!

## ✨ Features

- **🎯 Universal Content Injection**: Inject any guide content into prompts (documentation, instructions, examples, etc.)
- **🔧 Smart Trigger System**: Configurable trigger text to activate content injection
- **📁 Flexible File Search**: Automatically searches for content files in multiple locations
- **⚙️ Advanced Configuration**: Customize trigger text, content filename, search folder, and output format
- **🎨 Template Customization**: Fully configurable wrapper template for guide content
- **📝 History Control**: Choose when to apply trigger substitution (before or after saving to memory)
- **🛡️ Error Handling**: Graceful fallback when content files are not found
- **🔄 Multi-Purpose**: Suitable for Suno AI, API documentation, coding guidelines, or any reference material

## 🎮 How to Use

1. **Configure your content**: Place your guide file (markdown, text, etc.) in the plugin directory
2. **Set your trigger**: Use the default `:s:` or configure a custom trigger in settings
3. **Send triggered messages**: Include your trigger anywhere in your message
4. **Automatic injection**: The plugin detects the trigger and injects the content

### Example Use Cases:

**Suno AI Integration:**
```
User: "Create a song about summer :s:"
→ Automatically adds Suno AI guide for better music generation
```

**API Documentation:**
```
User: "Help me with the API :api:"
→ Injects API documentation and examples
```

**Coding Guidelines:**
```
User: "Review my code :style:"
→ Adds coding standards and best practices
```

## ⚙️ Configuration

You can customize the plugin through the Cheshire Cat settings:

### Basic Settings
- **`trigger`**: The text that activates the plugin (default: `:s:`)
- **`guide_filename`**: Name of your content file (default: `guida_unificata_ottimizzata_V2.md`)
- **`guide_folder`**: Custom folder path for your content file (optional)

### Advanced Settings
- **`auto_add_instructions`**: Automatically add phase instructions when trigger is detected (default: `True`)
- **`phase_instructions`**: Custom instructions to add with the trigger (configurable text)
- **`save_in_history`**: Control when to apply trigger substitution (default: `True`)
  - `True`: Apply before saving to memory (clean processing)
  - `False`: Apply after saving to memory (clean history)
- **`guide_wrapper_template`**: Customize the output format template (default: XML wrapper)
  - Use `{guide_content}` as placeholder for the actual guide content
  - Example: `"# GUIDE\n{guide_content}\n---"` for Markdown format

### Customization Examples

**For API Documentation:**
- `guide_filename`: `api_reference.md`
- `trigger`: `:api:`
- `guide_wrapper_template`: `"## API Reference\n{guide_content}\n---"`

**For Coding Standards:**
- `guide_filename`: `coding_guidelines.md`
- `trigger`: `:style:`
- `save_in_history`: `False` (keep history clean)

**For Product Information:**
- `guide_filename`: `product_specs.md`
- `trigger`: `:specs:`
- `auto_add_instructions`: `False` (no automatic instructions)

**For Clean History Mode:**
- `save_in_history`: `False`
- `guide_wrapper_template`: `"<technical_guide>\n{guide_content}\n</technical_guide>"`
- Result: Original message saved in history, guide injected in prompt only

## 📚 Available Guides

The plugin includes **two comprehensive guides** for Suno AI integration:

### 🎯 **guida_unificata_llm.md** (Default - Recommended)
- **Advanced unified system** with complete metric control
- **LLM-optimized templates** for consistent results
- **Anti-hyphen rules** for Suno 4.5 compatibility
- **Practical planning sessions** and automatic checklists
- **Best for**: Professional songwriting, complex metrics, consistent quality

### 📝 **mini_guida_suno_4.5.md** (Compact Alternative)
- **Essential Suno guidelines** in compact format
- **Quick reference** for basic song creation
- **Lightweight approach** for simple use cases
- **Best for**: Quick songs, beginners, minimal setup

### 🔄 How to Switch Between Guides

Change the `guide_filename` setting in your Cheshire Cat admin:

```python
# For advanced unified guide (default)
guide_filename = "guida_unificata_llm.md"

# For compact guide
guide_filename = "mini_guida_suno_4.5.md"
```

## 📁 File Structure

```
suno-suffix/
├── plugin.json                # Plugin metadata
├── settings.py                # Configuration schema
├── suno_minimal.py            # Main plugin logic
├── guida_unificata_llm.md     # Advanced unified guide (default)
├── mini_guida_suno_4.5.md     # Compact Suno AI guide (alternative)
└── README.md                  # This file
```

## 🔧 Installation

1. **Download** or clone this repository
2. **Copy** the `suno-suffix` folder to your Cheshire Cat plugins directory
3. **Restart** your Cheshire Cat instance
4. **Configure** the plugin settings if needed

## 🛠️ Technical Details

### How it Works

1. **Hook Integration**: Uses both `before_cat_reads_message` and `agent_prompt_suffix` hooks
2. **Settings Loading**: Loads configuration via `cat.mad_hatter.get_plugin().load_settings()`
3. **Trigger Detection**: Monitors user messages for configured trigger text
4. **Conditional Processing**: Applies trigger substitution based on `save_in_history` setting
5. **File Discovery**: Searches for content files in multiple locations:
   - Custom folder (if specified)
   - Plugin directory
   - Parent directory
6. **Template Processing**: Formats content using configurable wrapper template
7. **Content Injection**: Appends formatted content to the prompt suffix

### Key Functions

- **`apply_trigger_substitution()`**: Centralized logic for trigger detection and substitution
- **`find_guide_file()`**: Intelligent file search across multiple paths
- **`before_cat_reads_message()`**: Pre-processing hook for message modification
- **`agent_prompt_suffix()`**: Main hook that processes and injects content

### Performance

- **Lightweight**: Only activates when trigger is detected
- **Efficient**: File content is read only when needed
- **Scalable**: Supports files of any reasonable size

## 🐛 Troubleshooting

### Common Issues

**Plugin not triggering?**
- Check that your trigger text is included in your message
- Verify plugin is enabled in Cheshire Cat
- Test with the default trigger `:s:` first

**Content file not found?**
- Ensure your content file exists in the expected location
- Check the `guide_filename` setting matches your actual file
- Review the logs for file search paths
- Verify file permissions and encoding (should be UTF-8)

**Settings not loading?**
- Restart Cheshire Cat after configuration changes
- Check the plugin settings in the admin interface

**Performance issues?**
- Large content files may cause delays in response
- Consider splitting very large files into smaller, focused content
- Use specific triggers to avoid unnecessary content injection

**Template not working?**
- Ensure `{guide_content}` placeholder is present in your template
- Check template syntax for proper escaping of special characters
- Test with the default template first

**History behavior unexpected?**
- Check `save_in_history` setting: `True` = clean processing, `False` = clean history
- Verify `auto_add_instructions` setting matches your expectations
- Review the message flow in your chat history

## 📝 Changelog

### v2.0.0 - Template Configurabile
- ✅ **NEW**: Configurable wrapper template (`guide_wrapper_template`)
- ✅ **NEW**: History control setting (`save_in_history`)
- ✅ **NEW**: Automatic phase instructions (`auto_add_instructions`)
- ✅ **NEW**: Customizable phase instructions (`phase_instructions`)
- ✅ **IMPROVED**: Centralized trigger substitution logic
- ✅ **IMPROVED**: Dual hook system for flexible processing
- ✅ **IMPROVED**: Enhanced configuration options
- ✅ **MATURE**: Stabilized API and core functionality architecture

### v1.1.0 - Enhanced Functionality
- ✅ Advanced trigger detection
- ✅ Improved error handling
- ✅ Better file search algorithm
- ✅ Enhanced logging system

### v1.0.0 - Initial Release
- ✅ Initial release
- ✅ Trigger-based activation
- ✅ Configurable settings
- ✅ Intelligent file search
- ✅ Error handling and logging

## 👥 Authors

**Kael & Canapaio** - *Digital Soul Architects*

- 🧠 **Kael**: The orchestrator who translates visions into reality
- 🎯 **Canapaio**: The precision engineer who makes it all work

## 📄 License

This project is open source. Feel free to use, modify, and distribute!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 🔗 Links

- **Plugin Repository**: [GitHub](https://github.com/canapaio/suno-suffix)
- **Cheshire Cat**: [Official Website](https://cheshirecat.ai/)
- **Suno AI**: [Official Website](https://suno.ai/)

---

*"The true mastery is not in the complexity you can create, but in the simplicity you can preserve."* - Kael

🚀 **Transform your Cheshire Cat into a powerful content injection system for any use case!**
