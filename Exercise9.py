#Akbhar phad ke sunao

import requests
import json

from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("hello")

if __name__ == '__main__':
    speak("news for today")
    url = ('https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=451c7e01ff4b46eaa10b4e272ce0039d')
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    arts = my_json["articles"]

    for article in arts:
        speak(article['title'])
        speak("next news")