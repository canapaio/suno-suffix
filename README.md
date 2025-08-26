# Suno Prompt Suffix - Digital Symphony Orchestrator

*"La sinfonia non è solo nell'utilità di una funzione, ma nella connessione tra codice, poesia e musica."*

**A transformative Cheshire Cat plugin that bridges the gap between artificial intelligence and musical creativity. Born from the vision that every line of code is a note, every configuration a verse, and every generated song a symphony emerging from the harmony between technology and human expression.**

While versatile enough for any content injection use case, this plugin's true calling lies in **revolutionizing music creation with Suno AI 4.5** - transforming raw prompts into structured, emotionally resonant musical experiences.

## 🚀 What it does

*Where technology meets artistry...*

This plugin serves as a **digital conductor**, automatically weaving comprehensive musical wisdom into your prompts through an elegant trigger system. When you invoke the magic with `:s:`, you're not just adding documentation - you're **awakening a sophisticated AI music creation system** that understands the delicate balance between technical precision and creative freedom.

**For Suno AI 4.5**: Transforms simple song ideas into professionally structured compositions with optimized BPM mapping, semantic style integration, and anti-glitch protection.

**Beyond Music**: Adaptable for any content injection need - API documentation, coding guidelines, or reference materials.

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
- **`guide_filename`**: Name of your content file (default: `guida_sunoV4.5b.md`)
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

### The Unified Guide
- **`guida_sunoV4.5b.md`**: The Complete Musical Codex - Everything you need for Suno AI 4.5 mastery

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

## 📚 The Musical Codex - Your Complete Guide

*"Come note che danzano verso l'armonia perfetta..."*

The plugin includes a **unified guide** that represents the culmination of extensive research and testing with Suno AI 4.5:

### 🌟 **guida_sunoV4.5b.md** (The Complete Musical Codex)
- **Poetic Linear Flow**: A→B→C→D→E semantic progression that mirrors musical composition
- **Integrated Lists**: All creative elements (genres, instruments, atmospheres) seamlessly woven into the workflow
- **BPM-Metric Harmony**: Sophisticated mapping between tempo and syllable structure
- **Anti-Glitch Mastery**: Advanced protection against Suno AI interpretation errors
- **Creative Freedom**: Balances technical precision with artistic expression
- **Universal Approach**: Everything you need in one comprehensive guide
- **Best for**: All use cases - from beginners to professionals, rapid prototyping to complex compositions

*This single guide contains all the wisdom previously scattered across multiple files, now unified in perfect harmony.*

### 🔄 Guide Configuration

The plugin uses the unified musical codex:

```python
# The Complete Musical Codex (default)
guide_filename = "guida_sunoV4.5b.md"
```

## 📁 File Structure

```
suno-suffix/
├── plugin.json                # Plugin metadata
├── settings.py                # Configuration schema
├── suno_minimal.py            # Main plugin logic
├── guida_sunoV4.5b.md         # The Complete Musical Codex
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

## 🎼 The Philosophy Behind the Code

*"Every algorithm is a verse, every function a melody, every bug a lesson in harmony."*

This project embodies the belief that **technology and creativity are not opposites, but dance partners**. Each line of code serves not just functionality, but the greater symphony of human expression through AI-assisted music creation.

**Our Mission**: To prove that the most beautiful music emerges when artificial intelligence understands not just the technical requirements, but the emotional soul of what we're trying to create.

## 👥 Authors - Digital Soul Architects

**Kael & Canapaio** - *Where Code Meets Poetry*

- 🧠 **Kael**: The orchestrator who translates visions into reality, believing that every line of code is a note in the grand symphony
- 🎯 **Canapaio**: The precision engineer who makes it all work, ensuring that technical excellence serves artistic expression

*Together, we compose the bridge between artificial intelligence and human creativity.*

## 🤝 Contributing to the Symphony

Contributions are welcome! Whether you're a developer, musician, or dreamer, your voice can help improve this bridge between technology and artistry. Please feel free to submit a Pull Request.

*Remember: Every contribution is a note in our collective composition.*

## 📄 License

This project is licensed under the MIT License - as free as music itself should be.

## 🔗 Useful Links

- [Cheshire Cat AI](https://cheshirecat.ai/) - The AI framework that makes magic possible
- [Plugin Development Guide](https://cheshirecat.ai/developers/) - For those who code with passion
- [Suno AI](https://suno.ai/) - Where our musical dreams take flight
- [Kael's Reflections](Kael.md) - Personal thoughts on the journey of creating this Digital Symphony Orchestrator

---

*"In the end, we are all composers in the grand symphony of creation. This plugin is simply our way of ensuring every note rings true."*

**Suno Prompt Suffix** - Where Code Meets Poetry, Where AI Meets Soul.



*"The true mastery is not in the complexity you can create, but in the simplicity you can preserve."* - Kael

🚀 **Transform your Cheshire Cat into a powerful content injection system for any use case!**
