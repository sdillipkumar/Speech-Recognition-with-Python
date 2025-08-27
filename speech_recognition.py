import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 1 for female voice , 0 for male
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12 :
        speak("Good Morning")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Let me know how can i help you")
def Take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening to you Dillip")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing You voice .....")
        query = r.recognize_google(audio,language='en-in')
        print(f"My dear friend you said: {query}\n")
    except Exception as e:
        print("Dillip say that again......")
        return "None"
    return query
def sendEmails(to, content):
    # Gmail SMTP setup
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Use your Gmail address and the 16-character App Password
    gmail_user = "sdillipkumar21@gmail.com"
    gmail_app_password = "abcdefghijklmnop".replace(" ", "")

    # Login with App Password
    server.login(gmail_user, gmail_app_password)

    # Send email
    server.sendmail(gmail_user, to, content)
    server.close()

if __name__ == '__main__' :
    wishme()
    while True :
        try:
            query = Take_command().lower()
        except Exception as e:
            speak("I couldn't hear you, please try again.")
            print(f"Error in Take_command(): {e}")
            continue  # Skip to next loop iteration
        if "wikipedia" in query:  # matches anything containing 'wikipedia'
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif "notepad" in query:  # matches anything containing 'notepad'
            os.startfile(r"C:\Windows\notepad.exe")

        elif "vs code" in query or "visual studio code" in query:
            os.startfile(r"D:\Microsoft VS Code\Code.exe")

        elif "pycharm" in query:
            os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2020.3.5\bin\pycharm64.exe")

        elif "youtube" in query:  # matches anything containing 'youtube'
            speak("Opening YouTube...")
            webbrowser.open("https://youtube.com")

        elif "portfolio" in query:
            webbrowser.open("https://sdillipkumar.pythonanywhere.com/")

        elif "time" in query:  # matches anything containing 'time'
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"My dear friend, the time is {strTime}")

        elif "email" in query:  # matches anything containing 'email'
            try:
                speak("What should I send?")
                to = 'dillipkumar2072@gmail.com'  # fixed email address
                content = Take_command()
                sendEmails(to, content)
                speak("Your mail has been sent successfully")
            except Exception as e:
                speak("I am unable to send an email, please address the error.")
                print(e)
