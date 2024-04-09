import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import os
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    listener.pause_threshold = 2
    try:
        with sr.Microphone() as voice:
            talk("i ma your jazz,   'sir'  tell me your work today")
            print("listening...")
            command = listener.listen(voice)
        command = listener.recognize_google(command, language="en")
        talk(" {}".format(command))
        return command
    except Exception as e:
        print(e)
        pass


def check(command):
    print(command)
    if "Alexa" in command:
        command = command.replace("Alexa", "")
        print(command)
    if "time" in command:
        time = print(datetime.datetime.now())
        talk("current time is")
        talk(time)
    if "who is the" in command:
        person = command.replace("who is the", "")
        info = wikipedia.summary(person, sentences=4)
        print(info)
        talk(info)
    if "joke" in command:
        talk(pyjokes.get_joke())
    if "play" or "youtube" in command:
        print("playing")
        song = command.replace("play", "")
        song = command.replace("youtube", "")
        talk("plying")
        pywhatkit.playonyt(song, open_video=True)  # type: ignore
    if "sleep" in command:
        os.system("shutdown /s")


command = take_command()
check(command)
