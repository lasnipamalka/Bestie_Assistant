import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('I AM YOUR BESTIE.. How can I help you')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Bestie' in command:
                command = command.replace('Bestie', '')
                print(command)
    except:
        pass
    return command


def run_tweety():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        detail = command.replace('The details of', '')
        info = wikipedia.summary(detail, 1)
        if True:
            print(info)
            talk(info)
        else:
            talk('Sorry, Can you repeat again')
    elif 'stop' in command:
        assert isinstance(command, object)
        exit(command)
    else:
        talk('I am really sorry,Please say it again')


while True:
    run_tweety()
