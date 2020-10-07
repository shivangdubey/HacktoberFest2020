import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    if hour > 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello, I am JARVIS. How may I help you")

def takeCommand():
    #takes microphone input from the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('soham.naigaonkar@gmail.com', 'nasaisro')
    server.sendmail('soham.naigaonkar@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'what is your name' in query or 'who are you' in query:
            speak("I am Jarvis Desktop assistant and i was made by Soham.."
                  "How may I help you?")
        elif 'wikipedia' in query:
            speak("Searching wikipedia.....")
            print("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open gaana' in query:
            webbrowser.open('gaana.com')

        elif 'play music' in query:
            music_dir = r'C:\Users\91962\Desktop\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strTime}")

        elif 'open powerpoint' in query:
            path = r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE'
            os.startfile(path)

        elif 'open word' in query:
            path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(path)

        elif 'open chrome' in query:
            path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(path)

        elif 'open zoom' in query:
            path = r"C:\Users\91962\AppData\Roaming\Zoom\bin\Zoom.exe"
            os.startfile(path)

        elif 'email to soham' in query:
            try:
                speak("What should I send?")
                print("What should I send?\n")
                content = takeCommand()
                to = "soham.naigaonkar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Something went wrong please try again")

        # elif 'quit' or 'mic off' or 'i dont want to talk with you' in query:
        #     speak("Nice Talking to you")
        #     exit()
