import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Jarvis: Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User: {query}\n")
            return query.lower()

        except Exception as e:
            return "none"

def listen_for_wakeup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Faster listen for wakeup
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            return query.lower()
        except:
            return "none"
