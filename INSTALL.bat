@echo off
title JARVIS v2.0 Installer
color 0B

echo.
echo  ╔══════════════════════════════════════════════╗
echo  ║   J.A.R.V.I.S  v2.0  INSTALLER              ║
echo  ║   Gmail + WhatsApp Desktop + GPT-4o          ║
echo  ╚══════════════════════════════════════════════╝
echo.

echo  [1/6] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found!
    echo  Download from https://python.org
    echo  CHECK "Add Python to PATH" during install!
    pause
    exit /b 1
)
python --version
echo.

echo  [2/6] Installing core AI packages...
python -m pip install openai SpeechRecognition pyttsx3 psutil requests --quiet --upgrade
echo  Done.

echo  [3/6] Installing PyAudio (microphone)...
python -m pip install pyaudio --quiet
if errorlevel 1 (
    python -m pip install pipwin --quiet
    pipwin install pyaudio --quiet
)
echo  Done.

echo  [4/6] Installing Windows automation (WhatsApp control)...
python -m pip install pywin32 pyautogui --quiet --upgrade
echo  Done.

echo  [5/6] Installing browser automation (Gmail)...
python -m pip install selenium webdriver-manager --quiet --upgrade
echo  Done.

echo  [6/6] All done!
echo.
echo  ════════════════════════════════════════════════
echo  NEXT: Add your OpenAI API key to jarvis.py
echo  Get key free at: platform.openai.com/api-keys
echo  Then run: START_JARVIS.bat
echo  ════════════════════════════════════════════════
echo.
pause
