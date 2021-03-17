from __future__ import print_function
from bedtime import computer_sleep
from diction import translate
from news import speak_news, getNewsUrl
from simple_tracker import scrape_amazon
from youtube import youtube
from threading import Event
from datetime import datetime
from sys import platform
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from kill_threads import StoppableThread
from decimal import *

import subprocess
import _thread
import json
import os
import smtplib
import sys
import webbrowser
import psutil
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import time
import loc

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
stop_event = Event()


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

    except Exception:
        # print(e)
        return 'None'
    return _query


def wish_me():
    hour = datetime.now().time().hour
    if 0 <= hour < 12:
        speak("Good Morning.")
    elif 12 <= hour < 18:
        speak("Good Afternoon.")

    else:
        speak('Good Evening.')
    loc.weather()
    speak('I am JARVIS, at your service sir.')


def send_email(_to, _content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', _to, _content)
    server.close()


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


def backup(name):
    print(name)
    return os.system("cd scripts/bat && spider.bat")


def backup_blender(name):
    return os.system("cd scripts/bat && spider-lite.bat blender")


def start_blender(name):
    return os.system("blender")


def spotify_open():
    return os.system("cd scripts/vbs && fav.vbs")


def change_volume(val):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMasterVolume(val, None)
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            break


def spotify_rand():
    change_volume(1)
    os.system("@echo off && @echo Loading... && cd scripts/bat && rand-spotify.bat")
    time.sleep(10)
    change_volume(0.9)
    time.sleep(0.1)
    change_volume(0.7)
    time.sleep(0.1)
    change_volume(0.5)
    time.sleep(0.1)
    change_volume(0.3)
    time.sleep(0.1)
    change_volume(0.1)
    speak('I generated a random list of songs on spotify and added them to the queue.')
    change_volume(0.2)
    time.sleep(0.1)
    change_volume(0.4)
    time.sleep(0.1)
    change_volume(0.6)
    time.sleep(0.1)
    change_volume(0.8)
    time.sleep(0.1)
    change_volume(1)
    while countdown_thread.stopped() is not True:
        time.sleep(60)


def spotify_play(song):
    change_volume(1)

    for i in range(10):
        proc = subprocess.Popen(["spotify", "play", song], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        album, all_artists, name = clean_song_string(out)
        time.sleep(15)
        if err:
            change_volume(0.9)
            time.sleep(0.1)
            change_volume(0.7)
            time.sleep(0.1)
            change_volume(0.5)
            time.sleep(0.1)
            change_volume(0.3)
            time.sleep(0.1)
            change_volume(0.1)
            speak(f'Ummm, Vicz, I ran into an error trying to open spotify. {err}')
            change_volume(0.2)
            time.sleep(0.1)
            change_volume(0.4)
            time.sleep(0.1)
            change_volume(0.6)
            time.sleep(0.1)
            change_volume(0.8)
            time.sleep(0.1)
            change_volume(1)
            time.sleep(2)
        else:
            print(all_artists, name, album, err)
            change_volume(0.9)
            time.sleep(0.1)
            change_volume(0.7)
            time.sleep(0.1)
            change_volume(0.5)
            time.sleep(0.1)
            change_volume(0.3)
            time.sleep(0.1)
            change_volume(0.1)
            speak(f'I am currently playing, {name} by {all_artists}. Album is {album}')
            change_volume(0.2)
            time.sleep(0.1)
            change_volume(0.4)
            time.sleep(0.1)
            change_volume(0.6)
            time.sleep(0.1)
            change_volume(0.8)
            time.sleep(0.1)
            change_volume(1)
            break

    while countdown_thread.stopped() is not True:
        time.sleep(60)

    exit(1)


def clean_song_string(out):
    song = out.decode("utf-8")
    name = song[9:]
    index = name.find("\r\n  ")
    name = name[:index]
    song = song[30:-2]
    divider = song.find(" - ")
    artists = song[:divider]
    artists = artists.split(',')
    if len(artists) > 1:
        all_artists = ""
        for x in artists:
            if x == artists[len(artists) - 1]:
                all_artists += "and "
                all_artists += x
            elif x == artists[len(artists) - 2]:
                all_artists += x
                all_artists += " "
            else:
                all_artists += x
                all_artists += ", "
    else:
        all_artists = artists
    album = song[divider + 2:]
    return album, all_artists, name


def execute_jarvis():
    if countdown_thread.stopped():
        time.sleep(10)
        exit(1)
    if platform == "win32":
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wish_me()
    animation = "|/-\\"
    idx = 0

    while True:
        if countdown_thread.stopped():
            time.sleep(10)
            exit(1)

        print(animation[idx % len(animation)], end='')
        idx += 1
        query = takeCommand().lower()

        if '223' in query:
            print(f'\nsaid: {query}\n')

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
                time.sleep(25)
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
                speak("Ok sir.")
                spotify_open_thread = StoppableThread(target=spotify_open)
                spotify_open_thread.start()
                speak("Hope you enjoy.")
                time.sleep(15)
                index = query.find("music")
                song = query[index + 5:]
                print(song)
                if song != "":
                    speak(f'Let me search for {song} on spotify')
                    spotify_play_thread = StoppableThread(target=spotify_play(song=song))
                else:
                    spotify_play_thread = StoppableThread(target=spotify_rand)

                spotify_play_thread.start()

            elif 'turn up the volume' in query:
                os.system("cd scripts/vbs && volup.vbs 5")
            elif 'turn it down' in query:
                os.system("cd scripts/vbs && vold.vbs 5")

            elif 'search youtube' in query:
                speak('What you want to search on Youtube?')
                youtube(takeCommand())
            elif 'the time' in query:
                strTime = datetime.now().strftime("%H:%M")
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
                    send_email(to, content)
                    speak('Email has been sent!')

                except Exception as e:
                    speak('Sorry sir, Not able to send email at the moment')

            elif 'i want you to sleep' in query:
                sys.exit()
        time.sleep(0.3)
        print(end='\r')


def time_ends():
    final_hour = 22
    final_minute = 30
    final_second = 5
    current = datetime.now().time()
    hour = current.hour
    minute = current.minute
    second = current.second
    final_time = 0
    total_seconds = (((final_hour * 60) + final_minute) * 60) + final_second
    current_seconds = (((hour * 60) + minute) * 60) + second

    if current_seconds < total_seconds:
        left = total_seconds - current_seconds
        final_time = left
        hour = int(left / (60 * 60))
        getcontext().prec = 6
        minute = (Decimal(left) / (Decimal(60) * (Decimal(60)))) - hour
        minute = Decimal(minute) * Decimal(60)
        second = minute - int(minute)
        minute = int(minute)
        second = int(second * 60)
        print("time left: ", hour.__str__() + ":" + minute.__str__() + ":" + second.__str__())
    else:
        print("my day is done Vicz!")

    return final_time


def countdown():
    my_timer = time_ends()

    for x in range(my_timer):
        my_timer = my_timer - 1
        time.sleep(1)
    print("See ya tomorrow!")
    countdown_thread.stop()
    if countdown_thread.stopped():
        exit(1)


if __name__ == '__main__':
    countdown_thread = StoppableThread(target=countdown)
    countdown_thread.start()
    time.sleep(1)
    execute_jarvis()
