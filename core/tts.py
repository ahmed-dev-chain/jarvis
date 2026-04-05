import os
import time
from gtts import gTTS
import pygame
from core.utils import silence_stderr

class TTSREngine:
    def __init__(self):
        # Silence ALSA noise during pygame initialization
        with silence_stderr():
            pygame.mixer.init()
        self.output_file = "speech.mp3"

    def speak(self, text):
        print(f"Jarvis: {text}")
        try:
            # Generate speech file using gTTS
            tts = gTTS(text=text, lang='en')
            tts.save(self.output_file)

            # Play the file using pygame
            pygame.mixer.music.load(self.output_file)
            pygame.mixer.music.play()

            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            # Unload before deleting
            pygame.mixer.music.unload()
            
            # Clean up the temporary file
            if os.path.exists(self.output_file):
                os.remove(self.output_file)

        except Exception as e:
            print(f"TTS Error: {e}")

    def stop(self):
        pygame.mixer.music.stop()

tts_engine = TTSREngine()

def speak(text):
    tts_engine.speak(text)

def stop_speech():
    tts_engine.stop()
