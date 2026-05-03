
╔══════════════════════════════════════════════════════════════╗
║        J.A.R.V.I.S  —  Desktop AI Assistant                 ║
║        Just A Rather Very Intelligent System                 ║
║        Powered by OpenAI GPT-4o  |  Full OS Control         ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 QUICK START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 WINDOWS:
   1. Double-click INSTALL.bat          (first time only)
   2. Open jarvis.py → add your API key
   3. Double-click START_JARVIS.bat

 MAC / LINUX:
   1. Run: bash install.sh              (first time only)
   2. Open jarvis.py → add your API key
   3. Run: ./start_jarvis.sh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 API KEY SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 1. Go to: https://platform.openai.com/api-keys
 2. Sign in / Sign up (free)
 3. Click "Create new secret key"
 4. Copy the key (starts with sk-...)
 5. Open jarvis.py in Notepad/VS Code
 6. Find this line near the top:
       OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"
 7. Replace with your key:
       OPENAI_API_KEY = "sk-abc123..."
 8. Save and run!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW TO USE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Just say "Jarvis" to wake him up, then speak your command!

 WAKE WORDS:
   "Jarvis"           "Hey Jarvis"
   "Ok Jarvis"        "Yo Jarvis"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 VOICE COMMANDS  (examples)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 APPS & SYSTEM:
   "Jarvis, open Settings"
   "Jarvis, open Calculator"
   "Jarvis, open Notepad"
   "Jarvis, open Spotify"
   "Jarvis, open Chrome"
   "Jarvis, open File Explorer"
   "Jarvis, take a screenshot"
   "Jarvis, lock the screen"

 VOLUME:
   "Jarvis, volume up"
   "Jarvis, volume down"
   "Jarvis, mute the volume"

 WEB:
   "Jarvis, search for Python tutorials"
   "Jarvis, open YouTube"
   "Jarvis, open Google"

 INFORMATION:
   "Jarvis, what's my battery level?"
   "Jarvis, what time is it?"
   "Jarvis, what's the weather today?"
   "Jarvis, tell me a joke"

 TASKS:
   "Jarvis, write me a Python function to sort a list"
   "Jarvis, help me write an email to my boss"
   "Jarvis, what is machine learning?"
   "Jarvis, translate hello to Spanish"

 TO STOP:
   "Jarvis, stop" or  Ctrl+C in terminal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 jarvis.py          Main program
 INSTALL.bat        Windows installer  (run first)
 START_JARVIS.bat   Windows launcher
 install.sh         Mac/Linux installer
 start_jarvis.sh    Mac/Linux launcher
 README.txt         This file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 "Microphone error"
   → Run INSTALL.bat again to install PyAudio
   → Windows: Allow microphone in Privacy Settings

 "ModuleNotFoundError"
   → Run INSTALL.bat (Windows) or install.sh (Mac/Linux)

 "Authentication error"
   → Your API key is wrong. Check it at:
     https://platform.openai.com/api-keys

 "No speech detected"
   → Speak clearly after JARVIS says "Yes?"
   → Check your microphone is set as default input

 JARVIS not hearing wake word
   → Speak clearly: "Jar-vis"
   → Reduce background noise
   → Check microphone volume in system settings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
