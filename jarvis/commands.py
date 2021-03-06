import speech_recognition as sr
import pyttsx3
from Global.print_talk import print_talk

# ################# For Commands #############################

import pywhatkit
import datetime
import pyjokes
from Tools.google import search
from Tools.google import wiki
from Tools.email_bot import get_email_info
import os

# ###########################################################

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def _take_command():
    try:
        with sr.Microphone() as source:
            print_talk('listening...')
            voice = listener.listen(source)
            command = ""
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        print('some error')
    return command


def _commands():
    command = _take_command()
    print(command)
    if 'play' in command:
        vid = command.replace('play', '')
        talk('playing ' + vid)
        pywhatkit.playonyt(vid)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print_talk('Current time is ' + time)
    elif any(item.lower() == command.lower() for item in ["what is", "how"]):
        print_talk("Results for " + command)
        q = command.replace('what is', '')
        search(q)
    elif 'lol' in command:
        talk('lol')
    elif 'idiot' in command:
        print_talk('u are a idiot?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'security' in command:
        from Tools.security_cam.security_cam import run
        run()
    elif 'hack' in command:
        os.startfile("C:/Users/Tanush/Personal/Other-Stuff/lol.bat")
    elif 'email' in command:
        e = input('what ur email: ')
        if e == '':
            e = "protanushsingh@gmail.com"
        print(e)
        p = input('Whats ur password: ')
        print(p)
        get_email_info(e, p)
    elif any(item.lower() == command.lower() for item in ["word", "note", "book"]):
        from Tools.word.word import Word
        Word()
    elif 'define' in command:
        try:
            q = command.replace('define', '')
            wiki(q)
        except:
            print_talk("Results for " + command)
            q = command.replace('define', '')
            search(q)
    elif any(item.lower() == command.lower() for item in ["quit", "stop", "shut up"]):
        quit()
    else:
        if command != "":
            print_talk("Results for " + command)
            search(command)
        else:
            print_talk("Please say the command again")
