import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import getpass
from bedtime import computer_sleep
from simple_tracker import scrape_amazon
import json
import _thread
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        _query = r.recognize_google(audio, language='en-gb')
        print(f'said: {_query}\n')

    except Exception:
        # print(e)
        return 'None'
    return _query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning.")
    elif 12 <= hour < 18:
        speak("Good Afternoon.")

    else:
        speak('Good Evening.')

    # weather()
    speak('I am JARVIS, at your service sir.')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + "%")

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent + "%")


def scraper():
    speak("Let me scan amazon on what prices they are offering for an iPhone 12. Just a sec...")
    scrape_amazon()
    f = open("reports/iphone 12.json", "r")
    y = json.loads(f.read())
    print(f'The cheapest iPhone 12 on amazon costs {y["currency"]} {y["best_item"]["price"]}')
    speak(f'The cheapest iPhone 12 on amazon costs {y["currency"]} {y["best_item"]["price"]}')
    speak("Would you like to purchase this product sir? I could do it for you?")
    query_ = takeCommand().lower()

    if 'yes' in query_:
        speak("Alright, here is the website")
        webbrowser.get('chrome').open_new_tab(y["best_item"]["url"])
        speak("I'll handle the payment for you. Expect a new iPhone 12 probably 2 days from now.")
    if 'no' in query_:
        speak("Ok i'll skip it. You do need a new phone sir. Just a tip.")


def joke():
    for i in range(2):
        speak(pyjokes.get_jokes()[i])


def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


def backup(name):
    print(name)
    return os.system("cd scripts/bat && spider.bat")


def backup_blender(name):
    return os.system("cd scripts/bat && spider-lite.bat blender")


def start_blender(name):
    return os.system("blender")


if __name__ == '__main__':

    if platform == "win32":
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    print('Listening...')

    while True:
        query = takeCommand().lower()

        if 'blender' in query:
            speak('Sure, setting up your desired workspace.')
            try:
                _thread.start_new_thread(backup_blender, ("b1",))
                _thread.start_new_thread(start_blender, ("b2",))
            except:
                speak("Am afraid I ran into an issue sir.")
                print("Error: unable to start thread")
            time.sleep(10)
            speak("Umm, Vicz, the upload source code wasn't compiled before hand.")
            time.sleep(5)
            speak("Ok, I'll compile the maven project and package it to a windows executable file.")
            time.sleep(50)
            speak("Your workspace is all setup sir")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        if 'are you there' in query:
            speak("Yes Sir, at your service")

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'open soundcloud' in query:
            webbrowser.get('chrome').open_new_tab('https://soundcloud.com/discover')
        elif 'open whatsapp' in query:
            webbrowser.get('chrome').open_new_tab('https://web.whatsapp.com/')
        elif 'upload' in query:
            # webbrowser.get('chrome').open_new_tab('https://fb.com')
            speak("Alright, I will watch the given directories for changes and backup to google servers")

            try:
                _thread.start_new_thread(backup, ("b1",))
            except:
                speak("Am afraid I ran into an issue sir.")
                print("Error: unable to start thread")

            speak("execution began")

        elif 'open blackboard' in query:
            webbrowser.get('chrome').open_new_tab('https://www.ole.bris.ac.uk/webapps/portal/execute/tabs/tabAction'
                                                  '?tab_tab_group_id=_17_1')
        elif 'cheapest iphone on amazon' in query:
            scraper()
        elif 'open cloud storage' in query:
            webbrowser.get('chrome').open_new_tab('https://console.cloud.google.com/home/dashboard?project=blender'
                                                  '-ableton-backup')
        elif 'open firebase' in query:
            webbrowser.get('chrome').open_new_tab('https://console.firebase.google.com/u/0/project/poultry101-6b1ed'
                                                  '/overview')

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')
        elif 'open presents' in query:
            webbrowser.get('chrome').open_new_tab('https://www.patreon.com/RicoPresents/posts')

        elif 'music' in query:
            speak("Ok, let me shuffle through spotify sir.")
            speak("Hope you enjoy.")
            os.system("cd scripts/vbs && fav.vbs")
        elif 'turn up the volume' in query:
            os.system("cd scripts/vbs && volup.vbs 5")
        elif 'turn it down' in query:
            os.system("cd scripts/vbs && vold.vbs 5")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            speak('ViczKing is my master. He created me couple of days ago')

        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'stand for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'open python' in query:
            if platform == "win32":
                os.startfile(
                    "D:\\pycharm\\app\\PyCharm 2020.1.1\\bin\\pycharm64.exe")
        elif 'open java' in query:
            if platform == "win32":
                speak("opening java")
                os.startfile(
                    "D:\\intelliJ\\app\\installed\\IntelliJ IDEA 2020.1.1\\bin\\idea64.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                speak("OK shutting windows down")
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                speak("OK shutting system down")
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/victorkingi')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember" + rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember that " + remember.read())

        elif 'go to sleep' in query:
            speak("Ok, I am putting windows to sleep mode sir")
            computer_sleep()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'email to gaurav' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'email'
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                speak('Sorry sir, Not able to send email at the moment')

        elif 'i want you to sleep' in query:
            sys.exit()
