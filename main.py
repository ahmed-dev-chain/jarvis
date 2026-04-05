import sys
from core.tts import speak
from core.stt import take_command, listen_for_wakeup
from features.datetime_info import tell_time, tell_date
from features.web_commands import open_google, open_youtube
from features.wikipedia_search import search_wikipedia

def main():
    print("Jarvis: Passive Mode (Listening for 'Jarvis')...")
    
    while True:
        # Passive listening for wakeup
        wakeup_query = listen_for_wakeup()

        if "jarvis" in wakeup_query:
            speak("Yes, sir? How can I help?")
            
            # Active mode for one command
            while True:
                query = take_command()

                if query == "none":
                    continue

                # Feature Routing using match (Python 3.10+)
                match query:
                    case q if "time" in q:
                        speak(tell_time())
                    case q if "date" in q:
                        speak(tell_date())
                    case q if "google" in q:
                        speak(open_google())
                    case q if "youtube" in q:
                        speak(open_youtube())
                    case q if "wikipedia" in q:
                        search_target = q.replace("wikipedia", "").strip()
                        if search_target:
                            speak(search_wikipedia(search_target))
                        else:
                            speak("What should I search for?")
                    case q if "goodbye" in q or "stop" in q or "exit" in q or "bye" in q:
                        speak("Goodbye, sir!")
                        sys.exit()
                    case q if "nothing" in q or "sleep" in q or "thank you" in q:
                        speak("Alright, sir. I'll be here if you need me.")
                        break # Go back to passive mode
                    case _:
                        speak("I'm not sure about that. Anything else?")
                
                # After one command, we can either break to passive or stay in active.
                # Let's break to passive for cleaner flow as requested.
                break
            
            print("Jarvis: Passive Mode (Listening for 'Jarvis')...")

if __name__ == "__main__":
    main()