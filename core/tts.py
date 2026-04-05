import pyttsx3
import threading
import queue

class TTSREngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 170)
        self.stop_requested = False

    def _speak(self, text):
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def speak(self, text):
        self._speak(text)

    def stop(self):
        self.engine.stop()

tts_engine = TTSREngine()

def speak(text):
    tts_engine.speak(text)

def stop_speech():
    tts_engine.stop()
