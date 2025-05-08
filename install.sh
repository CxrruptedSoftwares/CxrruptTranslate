#!/bin/bash

echo "Installing CxrruptTranslate..."

# Function to detect package manager
detect_package_manager() {
    if command -v apt-get &> /dev/null; then
        echo "apt"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v pacman &> /dev/null; then
        echo "pacman"
    elif command -v zypper &> /dev/null; then
        echo "zypper"
    else
        echo "unknown"
    fi
}

# Function to install Python and pip
install_python() {
    local pkg_manager=$(detect_package_manager)
    echo "Installing Python and pip using $pkg_manager..."
    
    case $pkg_manager in
        "apt")
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-venv
            ;;
        "dnf")
            sudo dnf install -y python3 python3-pip python3-virtualenv
            ;;
        "pacman")
            sudo pacman -S --noconfirm python python-pip
            ;;
        "zypper")
            sudo zypper install -y python3 python3-pip python3-virtualenv
            ;;
        *)
            echo "Unsupported package manager. Please install Python 3 and pip manually."
            exit 1
            ;;
    esac
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Attempting to install..."
    install_python
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Attempting to install..."
    install_python
fi

# Install system dependencies
echo "Installing system dependencies..."
case $(detect_package_manager) in
    "apt")
        sudo apt-get install -y python3-tk python3-dev
        ;;
    "dnf")
        sudo dnf install -y python3-tkinter python3-devel
        ;;
    "pacman")
        sudo pacman -S --noconfirm tk
        ;;
    "zypper")
        sudo zypper install -y python3-tk
        ;;
esac

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

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