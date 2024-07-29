import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            return ""

speak("Hello, how can I help you today?")

while True:
    command = listen()
    if 'hello' in command:
        speak("Hello there! How are you?")
    elif 'time' in command:
        from datetime import datetime
        speak(datetime.now().strftime("%H:%M:%S"))
    elif 'exit' in command:
        speak("Goodbye!")
        break
    else:
        speak("I didn't catch that.")
