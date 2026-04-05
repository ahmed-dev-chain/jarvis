# Jarvis - Modular Voice Assistant

A clean, modular Python-based voice assistant that listens for a wakeup word and responds to various commands.

## 🚀 Features

- **Wakeup Word**: Listens for 'Jarvis' in passive mode before activating.
- **Speech Recognition**: Uses Google's speech recognition for accurate command parsing.
- **Clean Command Handling**: Implements Python's `match` statement for streamlined command routing.
- **Modular Design**: Features are separated into their own modules for easy expansion.

### Current Commands
- 🕒 **Time & Date**: "What's the time?" / "What's the date?"
- 🌐 **Web Browsing**: "Open Google" / "Open YouTube"
- 📚 **Wikipedia**: "Search Wikipedia for [topic]"
- 🚪 **Exit**: "Goodbye", "Exit", "Stop", or "Bye".

## 🛠️ Project Structure

- `main.py`: Entry point and orchestration logic.
- `core/`:
    - `stt.py`: Speech-to-Text handler.
    - `tts.py`: Text-to-Speech handler.
- `features/`:
    - `datetime_info.py`: Time and date logic.
    - `web_commands.py`: Browser-based commands.
    - `wikipedia_search.py`: Knowledge retrieval.

## 📦 Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jarvis:
   ```bash
   python main.py
   ```

## 📝 Dependencies
- `pyttsx3`
- `SpeechRecognition`
- `wikipedia`
- `pyaudio` (for microphone input)
