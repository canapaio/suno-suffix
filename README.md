# Content Injection Plugin

**A versatile Cheshire Cat plugin that automatically injects guide content into prompts when triggered. While originally designed for Suno AI integration, this plugin can be adapted for any content injection use case.**

## 🚀 What it does

This plugin automatically adds comprehensive guide content to your prompt whenever you include a configurable trigger in your message. Perfect for injecting documentation, instructions, examples, or any reference material into your AI conversations!

## ✨ Features

- **🎯 Universal Content Injection**: Inject any guide content into prompts (documentation, instructions, examples, etc.)
- **🔧 Smart Trigger System**: Configurable trigger text to activate content injection
- **📁 Flexible File Search**: Automatically searches for content files in multiple locations
- **⚙️ Configurable Settings**: Customize trigger text, content filename, and search folder
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

- **`trigger`**: The text that activates the plugin (default: `:s:`)
- **`guida_filename`**: Name of your content file (default: `mini_guida_suno_4.5.md`)
- **`guida_folder`**: Custom folder path for your content file (optional)

### Customization Examples

**For API Documentation:**
- `guida_filename`: `api_reference.md`
- `trigger`: `:api:`

**For Coding Standards:**
- `guida_filename`: `coding_guidelines.md`
- `trigger`: `:style:`

**For Product Information:**
- `guida_filename`: `product_specs.md`
- `trigger`: `:specs:`

## 📁 File Structure

```
suno-suffix/
├── plugin.json             # Plugin metadata
├── settings.py             # Configuration schema
├── suno_minimal.py         # Main plugin logic
├── mini_guida_suno_4.5.md  # Default content file (Suno AI guide)
└── README.md              # This file
```

## 🔧 Installation

1. **Download** or clone this repository
2. **Copy** the `suno-suffix` folder to your Cheshire Cat plugins directory
3. **Restart** your Cheshire Cat instance
4. **Configure** the plugin settings if needed

## 🧪 Testing

Run the included test to verify everything works:

```bash
cd suno-suffix
python test_plugin.py
```

## 🛠️ Technical Details

### How it Works

1. **Hook Integration**: Uses Cheshire Cat's `agent_prompt_suffix` hook
2. **Settings Loading**: Loads configuration via `cat.mad_hatter.get_plugin().load_settings()`
3. **File Discovery**: Searches for content files in multiple locations:
   - Custom folder (if specified)
   - Plugin directory
   - Parent directory
4. **Content Injection**: Appends content to the prompt suffix

### Key Functions

- **`find_guida_file()`**: Intelligent file search across multiple paths
- **`agent_prompt_suffix()`**: Main hook that processes user messages

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
- Check the `guida_filename` setting matches your actual file
- Review the logs for file search paths
- Verify file permissions and encoding (should be UTF-8)

**Settings not loading?**
- Restart Cheshire Cat after configuration changes
- Check the plugin settings in the admin interface

**Performance issues?**
- Large content files may cause delays in response
- Consider splitting very large files into smaller, focused content
- Use specific triggers to avoid unnecessary content injection

## 📝 Changelog

### v1.0.0
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

- **Plugin Repository**: [GitHub](https://github.com/kael-canapaio/suno-minimal)
- **Cheshire Cat**: [Official Website](https://cheshirecat.ai/)
- **Suno AI**: [Official Website](https://suno.ai/)

---

*"The true mastery is not in the complexity you can create, but in the simplicity you can preserve."* - Kael

🚀 **Transform your Cheshire Cat into a powerful content injection system for any use case!**