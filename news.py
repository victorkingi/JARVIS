import json
import pyttsx3
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=gb&'
           'apiKey=1d86997714094133900a7ff69016437c')
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak("Today's Headlines are..")

    for index, articles in enumerate(arts):
        print(articles["source"]["name"])
        print(articles['title'])
        print(articles['description'])
        print(articles['url'])

        speak('From ' + articles["source"]["name"])
        speak(articles['title'])
        speak(articles['description'])

        if index == len(arts) - 1:
            break
    speak('These were the top headlines, Have a nice day Sir!!..')


if __name__ == '__main__':
    speak_news()


def getNewsUrl():
    return ('http://newsapi.org/v2/top-headlines?'
            'country=gb&'
            'apiKey=1d86997714094133900a7ff69016437c')
