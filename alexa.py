import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

name = "alexa"
listener = sr.Recognizer()
txt2spch = pyttsx3.init()
voces = txt2spch.getProperty('voices')
txt2spch.setProperty('voice', voces[2].id)


def talk(text):
    txt2spch.say(text)
    txt2spch.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-US")
            command = command.lower()
            if name in command:
                command=command.replace(name,'')
                print(command)
                return command
            else:
                return None
    except:
        command = None
    
x = 1 
def run():
    y=0
    command = ""
    try:
        command = listen()
        if command == None in command:
            y=1
    except:
        y=1
    if y==0:
        if 'reproduce' in command:
            text = (command.replace("reproduce", ""))
            talk("reproduciendo"+ text)
            pywhatkit.playonyt(text)

        elif "hora" in command:
            hora = datetime.datetime.now().strftime("%H:%M %p")
            talk("son las "+hora)

        elif "busca" in command:
            buscar = command.replace("busca", "")
            wikipedia.set_lang("es")
            info = wikipedia.summary(buscar, 1)
            talk(info)

        elif "hola" in command:
            talk("hola, disfruta tu dia. carita feliz")
            
        elif "gracias" in command:
            talk("denada, siempre a la orden")

        elif "detente" in command or "para" in command:
            talk("Cerrando programa")
            global x
            x=0

        else:
            talk("no lo se, vuelve a intentarlo")
while x == 1:
    run()
