# CxrruptTranslate

![CxrruptTranslate](https://img.shields.io/badge/CxrruptTranslate-Purple-black)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A powerful and elegant translation tool designed specifically for VRChat users. CxrruptTranslate provides real-time translation capabilities with a beautiful purple and black theme, making it perfect for international communication in VRChat.

## ✨ Features

- 🎨 Modern and elegant purple/black UI theme
- 🌍 Support for 100+ languages
- ⚡ Real-time translation with configurable delay
- 🔄 Auto-translation and auto-send to VRChat
- 🎮 Direct OSC integration with VRChat
- 🎯 Language auto-detection
- 📝 Clean and intuitive interface
- 🚀 Fast and responsive performance

## 🛠️ Installation

### Windows
1. Download the repository
2. Run `install.bat` as administrator
3. Follow the on-screen instructions
4. A desktop shortcut will be created automatically

### Linux
1. Download the repository
2. Open terminal in the repository directory
3. Make the install script executable:
   ```bash
   chmod +x install.sh
   ```
4. Run the installation script:
   ```bash
   ./install.sh
   ```
5. The application will be available in your applications menu

## 🚀 Usage

1. Launch CxrruptTranslate
2. Configure OSC settings (default: 127.0.0.1:9000)
3. Select your source and target languages
4. Enable auto-translate if desired
5. Start typing in the input box
6. Translations will appear in real-time
7. Click "Send to VRChat" to send the translated text

### Auto-Translation
- Enable the "Auto Translate" checkbox
- Adjust the delay (100ms - 5000ms) to control translation frequency
- Text will automatically translate and send to VRChat

## 🔧 Configuration

### OSC Settings
- Default IP: 127.0.0.1
- Default Port: 9000
- Adjust these settings in the OSC Settings panel

### Translation Settings
- Source Language: Choose or use "Auto Detect"
- Target Language: Select your desired output language
- Auto-Translate: Enable/disable real-time translation
- Delay: Control translation frequency (100ms - 5000ms)

## 📋 Requirements

- Python 3.7 or higher
- PyQt6
- deep-translator
- python-osc
- VRChat with OSC enabled

## 🐛 Troubleshooting

1. **OSC Connection Issues**
   - Ensure VRChat is running
   - Verify OSC is enabled in VRChat settings
   - Check IP and port settings

2. **Translation Not Working**
   - Check your internet connection
   - Verify language selection
   - Try restarting the application

3. **Installation Problems**
   - Ensure Python 3.7+ is installed
   - Run installation script as administrator
   - Check system requirements

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- VRChat for OSC support
- Google Translate API
- PyQt6 team
- All contributors and users