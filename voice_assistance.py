import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                print(command)
    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:                   #to play music
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:         #to tell time
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'information' in command:            #to access wikipedia
        person=command.replace('infomation','')
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)
    elif 'joke' in command:          #to tell joke
        talk(pyjokes.get_joke())
while True:
    run_alexa()
    break