#!/bin/bash

echo "Installing CxrruptTranslate..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create desktop shortcut
echo "Creating desktop shortcut..."
cat > CxrruptTranslate.desktop << EOL
[Desktop Entry]
Version=1.0
Type=Application
Name=CxrruptTranslate
Comment=VRChat Translation Tool
Exec=$(pwd)/venv/bin/python $(pwd)/main.py
Icon=utilities-terminal
Terminal=false
Categories=Utility;
EOL

# Make the script executable
chmod +x CxrruptTranslate.desktop

# Move desktop shortcut to applications directory
if [ -d "$HOME/.local/share/applications" ]; then
    mv CxrruptTranslate.desktop "$HOME/.local/share/applications/"
    echo "Desktop shortcut created in applications menu"
else
    echo "Could not create desktop shortcut. Please move CxrruptTranslate.desktop to your applications directory manually."
fi

echo "Installation complete!"
echo "To run CxrruptTranslate, use: source venv/bin/activate && python main.py" 