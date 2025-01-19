import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# import requests
# pip freeze > requirements.txt
# pip install -r requirements.txt

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open darshan" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry! This Command is Under Process.")
        
    
if __name__ == '__main__':
    speak("Hey Boss! How Can I help You?")
    while True:
        # Listen for the eake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        # recognize speech using recognize_google
        print("recognizeing....")
        try :
            with sr.Microphone() as source:
                print("Please say something:")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if ("hello" in word.lower()): 
                speak("Hey Boss!")
                # Listen foe command
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    command = r.recognize_google(audio)
                    processCommand(command)
                    
        except Exception as e:
            print("Error; {0}".format(e))
            
