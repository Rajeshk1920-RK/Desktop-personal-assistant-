#!/bin/bash
# ╔══════════════════════════════════════════════════════╗
# ║   J.A.R.V.I.S  —  Linux/Mac Auto Installer          ║
# ╚══════════════════════════════════════════════════════╝

echo ""
echo " ╔══════════════════════════════════════════╗"
echo " ║   J.A.R.V.I.S  INSTALLER                ║"
echo " ╚══════════════════════════════════════════╝"
echo ""

OS="$(uname -s)"

echo " [1/4] Detected OS: $OS"
echo ""

echo " [2/4] Installing system dependencies..."
if [ "$OS" = "Linux" ]; then
    sudo apt-get update -qq
    sudo apt-get install -y python3-pip portaudio19-dev python3-pyaudio ffmpeg -qq
elif [ "$OS" = "Darwin" ]; then
    if ! command -v brew &>/dev/null; then
        echo " Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install portaudio ffmpeg
fi
echo " OK"
echo ""

echo " [3/4] Installing Python packages..."
pip3 install openai SpeechRecognition pyttsx3 psutil requests pyaudio
echo " OK"
echo ""

echo " [4/4] Making scripts executable..."
chmod +x start_jarvis.sh
echo " OK"
echo ""

echo " ═══════════════════════════════════════════"
echo " NEXT STEP: Add your OpenAI API key"
echo " ───────────────────────────────────────────"
echo " 1. Open jarvis.py in any text editor"
echo " 2. Find: OPENAI_API_KEY = \"YOUR_OPENAI_API_KEY_HERE\""
echo " 3. Replace with your key from:"
echo "    https://platform.openai.com/api-keys"
echo " 4. Save the file"
echo " 5. Run: ./start_jarvis.sh"
echo " ═══════════════════════════════════════════"
echo ""
