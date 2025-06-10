import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f1c8bb90264a4e3b9dbc37041ea163e2"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ProcessCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif "news" in c:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            speak("Here are the top headlines.")
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Failed to fetch news.")
    else:
        speak("Sorry, I did not understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    try:
        while True:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis is listening...")
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)

                    if command.lower() in ["exit", "quit", "stop"]:
                        speak("Goodbye!")
                        break

                    ProcessCommand(command)

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except Exception as e:
        print(f"Error: {e}")
