# 🦾 Jarvis - Modular Voice Assistant

A highly responsive, modular Python-based voice assistant that listens for a wakeup word and responds to various commands with high-quality audio.

---

## 🚀 Key Features

- **Wakeup Word**: Listens for **'Jarvis'** in passive mode before activating.
- **High-Quality Speech**: Uses **Google Text-to-Speech (gTTS)** combined with **pygame-ce** for a smooth, natural voice.
- **Clean Terminal Experience**: Automatically suppresses common ALSA/JACK audio warnings during startup.
- **Snappy Command Processing**: Efficient command routing with Python's modern `match` statement.
- **Modular & Extensible**: Features are isolated into their own modules, making it easy to add your own skills.

### 🎙️ Current Skill Set
- 🕒 **Time & Date**: "What's the time?" / "What's the date?"
- 📚 **Wikipedia**: "Search Wikipedia for [topic]"
- 🌐 **Web Commands**: "Open Google" / "Open YouTube"
- 🚪 **System Controls**: "Goodbye", "Exit", "Nothing", or "Sleep".

---

## 🏗️ Architecture

- `main.py`: Core logic for passive/active mode switching.
- `core/`:
    - `stt.py`: Speech-to-Text (using SpeechRecognition).
    - `tts.py`: Text-to-Speech (using gTTS + pygame).
    - `utils.py`: System-level utilities (stderr suppression).
- `features/`:
    - `datetime_info.py`: Date and time retrieval.
    - `web_commands.py`: URL opening logic.
    - `wikipedia_search.py`: Knowledge base retrieval.

---

## 🛠️ Installation & Setup

### 1. Requirements
Ensure you have **FFmpeg** installed on your system for audio handling (especially on Linux).
```bash
sudo apt update && sudo apt install ffmpeg
```

### 2. Setup Virtual Environment
```bash
# Create and activate venv
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Jarvis
```bash
python main.py
```

---

## 🧪 Usage Tips
- **Passive Mode**: Jarvis stays quiet until he hears his name. Once activated, he will prompt you for a command.
- **Ambient Noise**: If you are in a noisy room, Jarvis will auto-calibrate his microphone sensitivity the first time he starts.

---

## 📦 Tech Stack
- **Python 3.10+** (using `match` statements)
- **gTTS** (Google Text-to-Speech)
- **pygame-ce** (High-performance audio playback)
- **SpeechRecognition** (Google Web API Recognizer)
- **Wikipedia-API** (Knowledge retrieval)

---

## 📝 License
Feel free to use and extend this project for your own personal use!
