#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║   J.A.R.V.I.S  —  Desktop AI Assistant  v4.0        ║
║   Powered by GROQ + Llama3 (100% FREE & UNLIMITED)  ║
║   + Full Windows Control                             ║
║   + Gmail + WhatsApp Desktop                         ║
╚══════════════════════════════════════════════════════╝

SETUP:
  python -m pip install groq SpeechRecognition pyttsx3 psutil pyautogui pywin32 pillow

GET FREE GROQ KEY:
  1. Go to console.groq.com
  2. Sign up free
  3. Click API Keys -> Create API Key
  4. Paste below
"""

import os, sys, time, subprocess, webbrowser
import platform, datetime, re
import speech_recognition as sr
import pyttsx3
import psutil

# ══════════════════════════════════════════════
#  🔑  PASTE YOUR GROQ API KEY HERE (FREE!)
#  Get it at: console.groq.com
# ══════════════════════════════════════════════
GROQ_API_KEY = "your api key "
# ══════════════════════════════════════════════

MODEL = "llama-3.3-70b-versatile"   # Free, fast, smart!
WAKE_WORDS = ["jarvis", "hey jarvis", "ok jarvis", "yo jarvis", "hi jarvis"]
OS_NAME    = platform.system()

# ── Colors ─────────────────────────────────
C  = "\033[96m"; B  = "\033[94m"; G  = "\033[92m"
Y  = "\033[93m"; R  = "\033[91m"; BO = "\033[1m"
D  = "\033[2m";  RS = "\033[0m";  M  = "\033[95m"

# ══════════════════════════════════════════════
#  SYSTEM PROMPT
# ══════════════════════════════════════════════
SYSTEM_PROMPT = """You are JARVIS — Tony Stark's personal AI assistant running on Windows.
Execute commands using special tags. Be sharp, concise, confident, slightly witty.
Keep spoken replies SHORT and natural — no markdown, no bullet points, no lists.

COMMAND TAGS — use EXACTLY as shown:

APPS:
[OPEN_APP:settings]     [OPEN_APP:calculator]   [OPEN_APP:notepad]
[OPEN_APP:chrome]       [OPEN_APP:edge]         [OPEN_APP:firefox]
[OPEN_APP:explorer]     [OPEN_APP:taskmgr]      [OPEN_APP:spotify]
[OPEN_APP:discord]      [OPEN_APP:vlc]          [OPEN_APP:paint]
[OPEN_APP:cmd]          [OPEN_APP:word]          [OPEN_APP:excel]
[OPEN_APP:whatsapp]     [OPEN_APP:camera]        [OPEN_APP:store]
[OPEN_APP:powerpoint]   [OPEN_APP:teams]         [OPEN_APP:zoom]
[OPEN_APP:telegram]     [OPEN_APP:steam]         [OPEN_APP:obs]

WEB:
[OPEN_URL:https://youtube.com]
[SEARCH_WEB:search query here]

SYSTEM:
[VOLUME_UP]   [VOLUME_DOWN]   [VOLUME_MUTE]
[SCREENSHOT]  [LOCK_SCREEN]
[SHUTDOWN]    [RESTART]

EMAIL:
[SEND_EMAIL:email@example.com|Subject|Body of email]

WHATSAPP:
[SEND_WHATSAPP:Contact Name|Message to send]

RULES:
- ALWAYS use a command tag when user wants to open/do something
- For email/whatsapp: say "Message prepared, say send it to confirm or cancel to abort"
- For shutdown/restart: always confirm first
- Current time: {TIME}
- Be conversational, sound like a real AI assistant
"""

# ══════════════════════════════════════════════
#  VOICE ENGINE
# ══════════════════════════════════════════════
class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        for v in voices:
            if any(x in v.name.lower() for x in ['david', 'mark', 'george', 'zira']):
                self.engine.setProperty('voice', v.id)
                break
        self.engine.setProperty('rate', 168)
        self.engine.setProperty('volume', 1.0)

    def say(self, text):
        clean = re.sub(r'\[[^\]]*\]', '', text).strip()
        clean = re.sub(r'\s+', ' ', clean)
        if clean:
            print(f"\n  {G}{BO}JARVIS ▶{RS} {G}{clean}{RS}\n")
            self.engine.say(clean)
            self.engine.runAndWait()

# ══════════════════════════════════════════════
#  EAR (Microphone)
# ══════════════════════════════════════════════
class Ear:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.rec.energy_threshold         = 250
        self.rec.dynamic_energy_threshold = True
        self.rec.pause_threshold          = 0.7
        self.mic = None
        try:
            self.mic = sr.Microphone()
            with self.mic as src:
                self.rec.adjust_for_ambient_noise(src, duration=1)
            print(f"  {G}✓ Microphone ready{RS}")
        except Exception as e:
            print(f"  {R}✗ Microphone error: {e}{RS}")
            print(f"  {Y}  Fix: python -m pip install pyaudio{RS}")

    def listen(self, timeout=5, limit=15):
        if not self.mic:
            return None
        try:
            with self.mic as src:
                audio = self.rec.listen(src, timeout=timeout, phrase_time_limit=limit)
            return self.rec.recognize_google(audio).lower().strip()
        except:
            return None

# ══════════════════════════════════════════════
#  APP LAUNCHER (Windows - FIXED!)
# ══════════════════════════════════════════════
class AppLauncher:
    APPS = {
        # Settings & System URIs
        "settings"          : ("uri",   "ms-settings:"),
        "wifi"              : ("uri",   "ms-settings:network-wifi"),
        "bluetooth"         : ("uri",   "ms-settings:bluetooth"),
        "display"           : ("uri",   "ms-settings:display"),
        "sound"             : ("uri",   "ms-settings:sound"),
        "battery"           : ("uri",   "ms-settings:batterysaver"),
        "windows update"    : ("uri",   "ms-settings:windowsupdate"),
        "update"            : ("uri",   "ms-settings:windowsupdate"),
        "privacy"           : ("uri",   "ms-settings:privacy"),
        "storage"           : ("uri",   "ms-settings:storagesense"),
        "apps"              : ("uri",   "ms-settings:appsfeatures"),
        "camera"            : ("uri",   "microsoft.windows.camera:"),
        "clock"             : ("uri",   "ms-clock:"),
        "store"             : ("uri",   "ms-windows-store:"),
        "photos"            : ("uri",   "ms-photos:"),
        "maps"              : ("uri",   "bingmaps:"),
        "mail"              : ("uri",   "outlookmail:"),
        "calendar"          : ("uri",   "outlookcal:"),
        "whatsapp"          : ("uri",   "whatsapp:"),
        # Shell commands
        "calculator"        : ("shell", "calc"),
        "notepad"           : ("shell", "notepad"),
        "paint"             : ("shell", "mspaint"),
        "wordpad"           : ("shell", "wordpad"),
        "explorer"          : ("shell", "explorer"),
        "file explorer"     : ("shell", "explorer"),
        "files"             : ("shell", "explorer"),
        "task manager"      : ("shell", "taskmgr"),
        "taskmgr"           : ("shell", "taskmgr"),
        "cmd"               : ("shell", "cmd"),
        "command prompt"    : ("shell", "cmd"),
        "terminal"          : ("shell", "wt"),
        "powershell"        : ("shell", "powershell"),
        "control panel"     : ("shell", "control"),
        "snipping tool"     : ("shell", "snippingtool"),
        "snip"              : ("shell", "snippingtool"),
        "magnifier"         : ("shell", "magnify"),
        "on screen keyboard": ("shell", "osk"),
        "keyboard"          : ("shell", "osk"),
        # Browsers
        "chrome"            : ("shell", "chrome"),
        "google chrome"     : ("shell", "chrome"),
        "firefox"           : ("shell", "firefox"),
        "edge"              : ("shell", "msedge"),
        "microsoft edge"    : ("shell", "msedge"),
        "brave"             : ("shell", "brave"),
        "opera"             : ("shell", "opera"),
        # Office
        "word"              : ("shell", "winword"),
        "microsoft word"    : ("shell", "winword"),
        "excel"             : ("shell", "excel"),
        "microsoft excel"   : ("shell", "excel"),
        "powerpoint"        : ("shell", "powerpnt"),
        "outlook"           : ("shell", "outlook"),
        "onenote"           : ("shell", "onenote"),
        # Media & Social
        "spotify"           : ("shell", "spotify"),
        "vlc"               : ("shell", "vlc"),
        "discord"           : ("shell", "discord"),
        "telegram"          : ("shell", "telegram"),
        "zoom"              : ("shell", "zoom"),
        "teams"             : ("shell", "teams"),
        "microsoft teams"   : ("shell", "teams"),
        "slack"             : ("shell", "slack"),
        "skype"             : ("shell", "skype"),
        "obs"               : ("shell", "obs64"),
        "steam"             : ("shell", "steam"),
        # Web shortcuts
        "gmail"             : ("web",   "https://mail.google.com"),
        "youtube"           : ("web",   "https://youtube.com"),
        "google"            : ("web",   "https://google.com"),
        "github"            : ("web",   "https://github.com"),
        "netflix"           : ("web",   "https://netflix.com"),
        "amazon"            : ("web",   "https://amazon.in"),
        "instagram"         : ("web",   "https://instagram.com"),
        "twitter"           : ("web",   "https://twitter.com"),
        "facebook"          : ("web",   "https://facebook.com"),
        "chatgpt"           : ("web",   "https://chat.openai.com"),
        "linkedin"          : ("web",   "https://linkedin.com"),
        "hotstar"           : ("web",   "https://hotstar.com"),
        "prime video"       : ("web",   "https://primevideo.com"),
        "reddit"            : ("web",   "https://reddit.com"),
    }

    def open(self, app_name):
        a = app_name.lower().strip()
        print(f"  {Y}🚀 Opening: {app_name}{RS}")

        # Direct match
        entry = self.APPS.get(a)

        # Fuzzy match
        if not entry:
            for key in self.APPS:
                if key in a or a in key:
                    entry = self.APPS[key]
                    break

        if entry:
            kind, target = entry
            try:
                if kind == "uri":
                    os.startfile(target)
                elif kind == "shell":
                    subprocess.Popen(target, shell=True)
                elif kind == "web":
                    webbrowser.open(target)
                print(f"  {G}✓ Opened: {app_name}{RS}")
                return True
            except Exception as e:
                print(f"  {R}✗ Error: {e} — trying fallback{RS}")
                try:
                    subprocess.Popen(app_name, shell=True)
                    return True
                except:
                    return False
        else:
            # Unknown — try shell directly
            try:
                subprocess.Popen(app_name, shell=True)
                print(f"  {G}✓ Attempted: {app_name}{RS}")
                return True
            except Exception as e:
                print(f"  {R}✗ Cannot open {app_name}: {e}{RS}")
                return False

# ══════════════════════════════════════════════
#  GMAIL BOT
# ══════════════════════════════════════════════
class GmailBot:
    def compose(self, to, subject, body):
        print(f"\n  {Y}📧 Opening Gmail compose...{RS}")
        url = (
            "https://mail.google.com/mail/?view=cm"
            f"&to={to.strip()}"
            f"&su={subject.strip().replace(' ', '+')}"
            f"&body={body.strip().replace(' ', '+').replace(chr(10), '%0A')}"
        )
        webbrowser.open(url)
        time.sleep(2)
        print(f"  {G}✓ Gmail compose opened!{RS}")
        print(f"  {C}  To:      {to}{RS}")
        print(f"  {C}  Subject: {subject}{RS}")
        print(f"  {C}  Body:    {body[:60]}{RS}")
        return True

    def send(self):
        try:
            import pyautogui
            pyautogui.FAILSAFE = False
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'enter')
            time.sleep(1)
            print(f"  {G}✓ Email sent!{RS}")
            return True
        except Exception as e:
            print(f"  {Y}⚠ Click Send in Gmail manually.{RS}")
            return False

# ══════════════════════════════════════════════
#  WHATSAPP DESKTOP BOT
# ══════════════════════════════════════════════
class WhatsAppBot:
    def _focus(self):
        try:
            import win32gui, win32con
            wins = []
            def cb(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    if 'whatsapp' in win32gui.GetWindowText(hwnd).lower():
                        wins.append(hwnd)
            win32gui.EnumWindows(cb, None)
            if wins:
                win32gui.ShowWindow(wins[0], win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(wins[0])
                time.sleep(0.8)
                return True
        except ImportError:
            pass
        return False

    def _open(self):
        print(f"  {Y}💬 Opening WhatsApp Desktop...{RS}")
        paths = [
            os.path.join(os.environ.get('LOCALAPPDATA', ''), 'WhatsApp', 'WhatsApp.exe'),
            os.path.join(os.environ.get('APPDATA', ''),      'WhatsApp', 'WhatsApp.exe'),
        ]
        for p in paths:
            if os.path.exists(p):
                subprocess.Popen([p])
                time.sleep(5)
                return
        os.startfile("whatsapp:")
        time.sleep(5)

    def prepare(self, contact, message):
        if not self._focus():
            self._open()
            time.sleep(2)
            self._focus()
        try:
            import pyautogui
            pyautogui.FAILSAFE = False
            # Search for contact
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1.5)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.3)
            pyautogui.typewrite(contact, interval=0.06)
            time.sleep(2.5)
            pyautogui.press('enter')
            time.sleep(1.5)
            # Type message
            pyautogui.press('escape')
            time.sleep(0.4)
            pyautogui.typewrite(message, interval=0.04)
            print(f"  {G}✓ WhatsApp message ready!{RS}")
            print(f"  {C}  Contact: {contact}{RS}")
            print(f"  {C}  Message: {message[:55]}{RS}")
            return True
        except ImportError:
            print(f"  {R}Run: python -m pip install pyautogui{RS}")
            return False
        except Exception as e:
            print(f"  {R}WhatsApp error: {e}{RS}")
            return False

    def send(self):
        try:
            import pyautogui
            pyautogui.press('enter')
            time.sleep(0.5)
            print(f"  {G}✓ WhatsApp message sent!{RS}")
            return True
        except Exception as e:
            print(f"  {R}Send error: {e}{RS}")
            return False

# ══════════════════════════════════════════════
#  VOLUME CONTROL
# ══════════════════════════════════════════════
def set_volume(action):
    keys = {"up": 175, "down": 174, "mute": 173}
    k = keys.get(action)
    if k:
        subprocess.run(
            ["powershell", "-c",
             f"$w=New-Object -ComObject WScript.Shell; $w.SendKeys([char]{k})"],
            shell=True, capture_output=True
        )
        print(f"  {G}✓ Volume {action}{RS}")

# ══════════════════════════════════════════════
#  SCREENSHOT
# ══════════════════════════════════════════════
def take_screenshot():
    ts  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(os.path.expanduser("~"), "Desktop", f"JARVIS_{ts}.png")
    try:
        from PIL import ImageGrab
        ImageGrab.grab().save(dst)
        print(f"  {G}📸 Saved: {dst}{RS}")
        return dst
    except ImportError:
        pass
    try:
        ps = (
            "Add-Type -AssemblyName System.Windows.Forms,System.Drawing;"
            "$s=[System.Windows.Forms.Screen]::PrimaryScreen.Bounds;"
            "$b=New-Object System.Drawing.Bitmap($s.Width,$s.Height);"
            "$g=[System.Drawing.Graphics]::FromImage($b);"
            "$g.CopyFromScreen($s.Location,[System.Drawing.Point]::Empty,$s.Size);"
            f"$b.Save('{dst}')"
        )
        subprocess.run(["powershell", "-c", ps], shell=True, capture_output=True)
        print(f"  {G}📸 Saved: {dst}{RS}")
        return dst
    except Exception as e:
        print(f"  {R}Screenshot error: {e}{RS}")
        return None

# ══════════════════════════════════════════════
#  GROQ BRAIN (FREE LLAMA3!)
# ══════════════════════════════════════════════
class Brain:
    def __init__(self, api_key):
        try:
            from groq import Groq
            self.client = Groq(api_key=api_key)
            self.history = []
            print(f"  {G}✓ Groq Llama3 brain ready (FREE & UNLIMITED){RS}")
        except ImportError:
            print(f"  {R}✗ Groq not installed!{RS}")
            print(f"  {Y}  Run: python -m pip install groq{RS}")
            sys.exit(1)

    def think(self, user_msg):
        now = datetime.datetime.now().strftime("%A %B %d %Y, %I:%M %p")
        prompt = SYSTEM_PROMPT.replace("{TIME}", now)
        self.history.append({"role": "user", "content": user_msg})
        # Keep last 20 messages
        if len(self.history) > 20:
            self.history = self.history[-20:]
        try:
            r = self.client.chat.completions.create(
                model    = MODEL,
                messages = [{"role": "system", "content": prompt}] + self.history,
                max_tokens  = 400,
                temperature = 0.8,
            )
            reply = r.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Brain error: {e}"

# ══════════════════════════════════════════════
#  COMMAND EXECUTOR
# ══════════════════════════════════════════════
class Executor:
    def __init__(self):
        self.launcher  = AppLauncher()
        self.gmail     = GmailBot()
        self.whatsapp  = WhatsAppBot()
        self.pending   = None  # "EMAIL" or "WHATSAPP"

    def run(self, response_text):
        tags = re.findall(r'\[([A-Z_]+)(?::([^\]]*))?\]', response_text)
        for tag, arg in tags:
            arg = arg.strip()
            print(f"  {Y}⚙  [{tag}] {arg[:50]}{RS}")
            self._do(tag, arg)

    def _do(self, tag, arg):
        try:
            if   tag == "OPEN_APP":    self.launcher.open(arg)
            elif tag == "OPEN_URL":    webbrowser.open(arg)
            elif tag == "SEARCH_WEB":  webbrowser.open("https://www.google.com/search?q=" + arg.replace(' ', '+'))
            elif tag == "VOLUME_UP":   set_volume("up")
            elif tag == "VOLUME_DOWN": set_volume("down")
            elif tag == "VOLUME_MUTE": set_volume("mute")
            elif tag == "SCREENSHOT":  take_screenshot()
            elif tag == "LOCK_SCREEN": subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
            elif tag == "SHUTDOWN":    subprocess.run(["shutdown", "/s", "/t", "15"])
            elif tag == "RESTART":     subprocess.run(["shutdown", "/r", "/t", "15"])
            elif tag == "SEND_EMAIL":
                parts = arg.split("|", 2)
                if len(parts) == 3:
                    to, sub, body = [p.strip() for p in parts]
                    if self.gmail.compose(to, sub, body):
                        self.pending = "EMAIL"
            elif tag == "SEND_WHATSAPP":
                parts = arg.split("|", 1)
                if len(parts) == 2:
                    contact, msg = [p.strip() for p in parts]
                    if self.whatsapp.prepare(contact, msg):
                        self.pending = "WHATSAPP"
        except Exception as e:
            print(f"  {R}Error [{tag}]: {e}{RS}")

    def confirm(self):
        if self.pending == "EMAIL":
            self.pending = None
            ok = self.gmail.send()
            return "Email sent successfully!" if ok else "Please click Send in Gmail."
        elif self.pending == "WHATSAPP":
            self.pending = None
            ok = self.whatsapp.send()
            return "WhatsApp message sent!" if ok else "Please press Enter in WhatsApp manually."
        self.pending = None
        return "Nothing to send."

    def cancel(self):
        p = self.pending
        self.pending = None
        return f"Cancelled. {p or 'Message'} was not sent."

# ══════════════════════════════════════════════
#  HUD DISPLAY
# ══════════════════════════════════════════════
def hud(state="STANDBY", you="", jarvis_txt="", waiting=None):
    os.system("cls")
    now = datetime.datetime.now()
    try:
        bat = psutil.sensors_battery()
        bs  = f"{bat.percent:.0f}%{'⚡' if bat.power_plugged else ''}" if bat else "N/A"
    except: bs = "N/A"
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    sc  = {"STANDBY":C, "LISTENING":R, "PROCESSING":Y,
           "SPEAKING":G, "WAITING":M}.get(state, C)

    print(f"{C}{'═'*62}{RS}")
    print(f"{C}  ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗{RS}")
    print(f"{C}  ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝{RS}")
    print(f"{C}  ██║███████║██████╔╝██║   ██║██║███████╗{RS}")
    print(f"{B}  ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║{RS}")
    print(f"{B}  ██║██║  ██║██║  ██║ ╚████╔╝ ██║███████║{RS}")
    print(f"{B}  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝{RS}")
    print(f"{C}{'═'*62}{RS}")
    print(f"  {D}Groq Llama3 (FREE) · Gmail · WhatsApp · {now.strftime('%H:%M:%S')}{RS}")
    print(f"{C}{'─'*62}{RS}")
    print(f"  {BO}STATUS{RS}  {sc}◉ {state}{RS}   {D}CPU:{cpu:.0f}% RAM:{ram:.0f}% BAT:{bs}{RS}")
    print(f"{C}{'─'*62}{RS}")
    if you:
        print(f"  {BO}YOU   ▶{RS} {M}{you[:56]}{RS}")
    if jarvis_txt:
        words = jarvis_txt.split(); line = ""; first = True
        for w in words:
            if len(line) + len(w) > 50:
                prefix = f"  {G}{BO}JARVIS▶{RS} {G}" if first else f"         {G}"
                print(f"{prefix}{line.strip()}{RS}")
                first = False; line = w + " "
            else:
                line += w + " "
        if line.strip():
            prefix = f"  {G}{BO}JARVIS▶{RS} {G}" if first else f"         {G}"
            print(f"{prefix}{line.strip()}{RS}")
    if waiting:
        print(f"{C}{'─'*62}{RS}")
        print(f"  {M}{BO}⏳ {waiting}{RS}")
        print(f"  {D}Say {C}\"send it\"{RS}{D} to confirm  |  {C}\"cancel\"{RS}{D} to abort{RS}")
    print(f"{C}{'─'*62}{RS}")
    print(f"  {D}Say {C}\"Jarvis\"{RS}{D} to wake  ·  Ctrl+C to exit{RS}")
    print(f"{C}{'═'*62}{RS}")

# ══════════════════════════════════════════════
#  MAIN JARVIS
# ══════════════════════════════════════════════
class JARVIS:
    CONFIRM = ["yes", "send it", "go ahead", "confirm", "do it",
               "send", "okay", "ok", "sure", "yep", "yeah", "correct"]
    CANCEL  = ["no", "cancel", "stop", "abort", "nope",
               "never mind", "nevermind", "don't send", "dont send"]

    def __init__(self):
        print(f"\n{C}  Starting J.A.R.V.I.S v4.0 (Groq Llama3 FREE){RS}\n")

        if not GROQ_API_KEY or GROQ_API_KEY == "YOUR_GROQ_API_KEY_HERE":
            print(f"{R}  ✗ Groq API key missing!{RS}")
            print(f"\n  {Y}Steps to get FREE key:{RS}")
            print(f"  1. Go to console.groq.com")
            print(f"  2. Sign up free")
            print(f"  3. Click API Keys → Create Key")
            print(f"  4. Open jarvis.py → paste key in GROQ_API_KEY")
            input(f"\n  Press Enter to exit...")
            sys.exit(1)

        self.voice  = Voice()
        self.ear    = Ear()
        self.brain  = Brain(GROQ_API_KEY)
        self.exe    = Executor()
        self.state  = "STANDBY"
        self.you    = ""
        self.jtext  = ""

        self._check_deps()
        hud()
        self._boot()

    def _check_deps(self):
        missing = []
        try: import pyautogui
        except: missing.append("pyautogui")
        try: import win32gui
        except: missing.append("pywin32")
        try: from PIL import ImageGrab
        except: missing.append("pillow")
        if missing:
            print(f"  {Y}⚠  Install for full features:{RS}")
            print(f"  {Y}   python -m pip install {' '.join(missing)}{RS}")
            time.sleep(2)

    def _boot(self):
        h = datetime.datetime.now().hour
        g = "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"
        msg = (f"{g}. J.A.R.V.I.S version 4 is online, powered by Llama 3. "
               f"I have full access to your Windows system, Gmail, and WhatsApp. "
               f"This service is completely free. Say my name to begin.")
        self.jtext = msg
        hud("SPEAKING", "", msg)
        self.voice.say(msg)
        hud("STANDBY", "", msg)

    def _process(self, command):
        self.you   = command
        self.state = "PROCESSING"
        hud("PROCESSING", command)

        reply = self.brain.think(command)
        self.exe.run(reply)

        clean = re.sub(r'\[[^\]]*\]', '', reply).strip()
        clean = re.sub(r'\s+', ' ', clean)
        self.jtext = clean

        waiting = None
        if self.exe.pending == "EMAIL":
            waiting = "📧 EMAIL ready — review in Gmail then say 'send it'"
        elif self.exe.pending == "WHATSAPP":
            waiting = "💬 WHATSAPP typed — say 'send it' to confirm"

        self.state = "SPEAKING"
        hud("SPEAKING", command, clean, waiting)
        self.voice.say(clean)

        if self.exe.pending:
            self.state = "WAITING"
            hud("WAITING", command, clean, waiting)
        else:
            self.state = "STANDBY"
            hud("STANDBY", command, clean)

    def run(self):
        while True:
            try:
                # ── WAITING FOR CONFIRM ──────────────
                if self.state == "WAITING" and self.exe.pending:
                    w = ("📧 EMAIL ready — say 'send it' to confirm"
                         if self.exe.pending == "EMAIL"
                         else "💬 WHATSAPP typed — say 'send it' to confirm")
                    hud("WAITING", self.you, self.jtext, w)
                    text = self.ear.listen(timeout=25, limit=8)
                    if text:
                        print(f"  {M}YOU: {text}{RS}")
                        if any(c in text for c in self.CONFIRM):
                            result = self.exe.confirm()
                            self.jtext = result
                            hud("SPEAKING", self.you, result)
                            self.voice.say(result)
                            self.state = "STANDBY"
                            hud("STANDBY", self.you, result)
                        elif any(c in text for c in self.CANCEL):
                            result = self.exe.cancel()
                            self.jtext = result
                            hud("SPEAKING", self.you, result)
                            self.voice.say(result)
                            self.state = "STANDBY"
                            hud("STANDBY", self.you, result)
                    continue

                # ── STANDBY — WAKE WORD ──────────────
                self.state = "STANDBY"
                heard = self.ear.listen(timeout=5, limit=5)
                if not heard:
                    continue
                if not any(w in heard for w in WAKE_WORDS):
                    continue

                # Exit command
                if any(x in heard for x in ["stop jarvis", "exit jarvis", "goodbye jarvis"]):
                    self.voice.say("Going offline. Goodbye.")
                    break

                # ── ACTIVATED ────────────────────────
                self.state = "LISTENING"
                hud("LISTENING")
                self.voice.say("Yes?")

                # ── GET COMMAND ──────────────────────
                cmd = self.ear.listen(timeout=10, limit=25)
                if not cmd or len(cmd) < 2:
                    self.voice.say("I didn't catch that. Call me again.")
                    self.state = "STANDBY"
                    hud("STANDBY", "", self.jtext)
                    continue

                # Remove wake word from command
                for w in WAKE_WORDS:
                    cmd = cmd.replace(w, "").strip()
                if not cmd:
                    continue

                self._process(cmd)

            except KeyboardInterrupt:
                print(f"\n{C}  J.A.R.V.I.S offline. Goodbye.{RS}\n")
                break
            except Exception as e:
                print(f"\n{R}  Error: {e}{RS}")
                time.sleep(1)

# ══════════════════════════════════════════════
#  START
# ══════════════════════════════════════════════
if __name__ == "__main__":
    j = JARVIS()
    j.run()
