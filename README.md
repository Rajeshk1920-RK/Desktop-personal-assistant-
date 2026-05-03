# Desktop-personal-assistant-
🤖 JARVIS — Voice-controlled AI desktop assistant powered by Groq Llama 3 (free). Say "Jarvis" to open apps, search the web, send emails, control volume, take screenshots &amp; more. Built with Python.


<div align="center">

```
██╗█████╗██████╗██╗  ██╗██╗    █ ██ █ █ █ █╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██║  ██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
```

# J.A.R.V.I.S — Desktop AI Assistant

**Just A Rather Very Intelligent System**

*Powered by Groq + Llama 3 · 100% Free & Unlimited · Full Windows Control*

---

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-Llama%203-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://console.groq.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://microsoft.com)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()

</div>

---

## 🤖 What is JARVIS?

JARVIS is a **voice-controlled desktop AI assistant** — inspired by Tony Stark's legendary AI — built in Python. It listens for its name, understands natural language commands, and takes real action on your computer. Powered entirely by **Groq's free Llama 3 API**, it gives you a fully intelligent, conversational assistant at **zero cost**.

> 💡 **Say "Jarvis" → give a command → watch it happen.**

---

## ✨ Features

| Category | Capability |
|---|---|
| 🗣️ **Voice Wake Word** | Activates on "Jarvis", "Hey Jarvis", "Ok Jarvis" |
| 🧠 **AI Brain** | Groq Llama 3.3-70B — fast, smart, free |
| 🖥️ **App Control** | Opens 30+ Windows apps by voice |
| 🌐 **Web Control** | Search Google, open any website |
| 📧 **Gmail** | Compose & send emails by voice |
| 💬 **WhatsApp** | Send WhatsApp Desktop messages hands-free |
| 🔊 **System Control** | Volume up/down/mute, screenshots, lock screen |
| 💬 **Conversation** | Ask anything — coding help, jokes, translations, weather |
| 🖥️ **Live HUD** | Real-time terminal dashboard with CPU, RAM, battery |
| ⚡ **Confirmation Flow** | Email/WhatsApp require voice confirmation before sending |

---

## 🚀 Quick Start

### Windows

```bash
# Step 1 — Install dependencies
INSTALL.bat

# Step 2 — Add your free Groq API key to jarvis.py
# Find: GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"

# Step 3 — Launch
START_JARVIS.bat
```

### Linux / macOS

```bash
# Step 1 — Install dependencies
bash install.sh

# Step 2 — Add your free Groq API key to jarvis.py

# Step 3 — Launch
./start_jarvis.sh
```

---

## 🔑 Get Your FREE API Key (30 seconds)

1. Go to **[console.groq.com](https://console.groq.com)**
2. Sign up free (no credit card)
3. Click **API Keys → Create API Key**
4. Open `jarvis.py` and paste it:

```python
GROQ_API_KEY = "gsk_your_key_here"
```

> ✅ Groq is **100% free** with generous rate limits. No billing required.

---

## 🎙️ Voice Commands

```
"Jarvis, open Settings"           → Opens Windows Settings
"Jarvis, open Chrome"             → Launches Google Chrome
"Jarvis, open Spotify"            → Opens Spotify
"Jarvis, search for Python tips"  → Googles it instantly
"Jarvis, take a screenshot"       → Saves screenshot to Desktop
"Jarvis, volume up"               → Increases system volume
"Jarvis, mute the volume"         → Mutes audio
"Jarvis, lock the screen"         → Locks Windows
"Jarvis, what's my battery?"      → Reads out battery %
"Jarvis, what time is it?"        → Tells current time
"Jarvis, send an email to..."     → Composes email via Gmail
"Jarvis, tell me a joke"          → Llama 3 delivers 🎭
"Jarvis, write a Python function" → AI coding assistant
"Jarvis, stop"                    → JARVIS goes offline
```

**Wake words:** `Jarvis` · `Hey Jarvis` · `Ok Jarvis` · `Yo Jarvis` · `Hi Jarvis`

---

## 📂 Project Structure

```
jarvis/
├── jarvis.py           ← Main program (all logic here)
├── INSTALL.bat         ← Windows one-click installer
├── START_JARVIS.bat    ← Windows launcher
├── install.sh          ← Linux/macOS installer
├── start_jarvis.sh     ← Linux/macOS launcher
└── README.md           ← You're here!
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.8+** | Core language |
| **Groq API + Llama 3.3-70B** | AI brain (free) |
| **SpeechRecognition** | Voice-to-text via Google |
| **pyttsx3** | Text-to-speech (offline) |
| **pyautogui** | Screen automation & screenshots |
| **pywin32** | Windows API control |
| **psutil** | CPU, RAM, battery stats |
| **selenium** | Gmail browser automation |

---

## 📦 Installation (Manual)

```bash
pip install groq SpeechRecognition pyttsx3 psutil pyautogui pywin32 pillow selenium webdriver-manager
```

> **PyAudio on Windows?** If `pip install pyaudio` fails:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🖥️ Live HUD Preview

```
══════════════════════════════════════════════════════════════
  ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
  ...
══════════════════════════════════════════════════════════════
  Groq Llama3 (FREE) · Gmail · WhatsApp · 14:32:05
──────────────────────────────────────────────────────────────
  STATUS  ◉ LISTENING   CPU:12% RAM:54% BAT:87%
──────────────────────────────────────────────────────────────
  YOU   ▶ open spotify
  JARVIS▶ Opening Spotify for you right now.
──────────────────────────────────────────────────────────────
  Say "Jarvis" to wake  ·  Ctrl+C to exit
══════════════════════════════════════════════════════════════
```

---

## 🔧 Troubleshooting

<details>
<summary><b>🎤 Microphone not working</b></summary>

- Run `INSTALL.bat` again to reinstall PyAudio
- Windows: Go to **Privacy Settings → Microphone** and allow access
- Check your microphone is set as the **default input device**

</details>

<details>
<summary><b>📦 ModuleNotFoundError</b></summary>

```bash
# Windows
INSTALL.bat

# Linux/macOS
bash install.sh
```

</details>

<details>
<summary><b>🔐 Authentication error</b></summary>

Your Groq API key is incorrect. Double-check it at [console.groq.com](https://console.groq.com) and make sure there are no spaces around it in `jarvis.py`.

</details>

<details>
<summary><b>🔇 JARVIS not responding to wake word</b></summary>

- Speak clearly: *"Jar-vis"*
- Reduce background noise
- Check microphone volume in system settings
- Wait for the **STANDBY** status on the HUD before speaking

</details>

---

## 🗺️ Roadmap

- [x] Voice wake word detection
- [x] Groq Llama 3 AI integration
- [x] Windows app control (30+ apps)
- [x] Gmail automation
- [x] WhatsApp Desktop automation
- [x] Live terminal HUD
- [ ] Image generation via voice
- [ ] News briefing ("Jarvis, morning briefing")
- [ ] Reminder & alarm system
- [ ] Linux/macOS full feature parity
- [ ] GUI dashboard

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Rajesh K**
- 🎓 Diploma in AI & Machine Learning — GTTC Magadi
- 💼 [LinkedIn](https://linkedin.com/in/your-profile)
- 🐙 [GitHub](https://github.com/your-username)
- 📧 your@gmail.com

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

*Built with ❤️ by Rajesh K · Inspired by Tony Stark's JARVIS*

**⭐ Star this repo if JARVIS impressed you!**

</div>
