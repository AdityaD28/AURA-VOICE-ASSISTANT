import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from datetime import datetime, timedelta
from fuzzywuzzy import process
import wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<your news api key"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key="<openai api key>")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named aura skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def getWeather(city):
    api_key = "<your openweathermap api key here>"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get("main"):
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degrees with {desc}.")
    else:
        speak("City not found.")

def wikiSearch(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except:
        # Fallback to ChatGPT if Wikipedia fails
        fallback_answer = aiProcess(query)
        speak(fallback_answer)


def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        parts = c.split(" ")
        if len(parts) < 2:
            speak("Please say the name of the song.")
        else:
            song_query = " ".join(parts[1:])
            song_names = list(musicLibrary.music.keys())
            best_match, score = process.extractOne(song_query.replace(" ", ""), song_names)
            if score >= 70:
                link = musicLibrary.music[best_match]
                speak(f"Playing {best_match}")
                webbrowser.open(link)
            else:
                speak("I couldn't find that song in your library.")
    elif "weather in" in c:
        city = c.split("in")[-1].strip()
        getWeather(city)
    elif "time" in c:
        speak(datetime.now().strftime("It's %I:%M %p"))
    elif "date" in c:
        speak(datetime.now().strftime("Today is %B %d, %Y"))
    elif "who is" in c or "what is" in c:
        topic = c.replace("who is", "").replace("what is", "").strip()
        wikiSearch(topic)
    elif "news" in c:
        try:
            today = datetime.now()
            from_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
            to_date = today.strftime('%Y-%m-%d')
            url = (
                f"https://newsapi.org/v2/everything?"
                f"q=India&from={from_date}&to={to_date}&language=en&sortBy=publishedAt&pageSize=5&apiKey={newsapi}")
            r = requests.get(url)
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles[:5]:
                    speak(article['title'])
            else:
                speak("No fresh Indian news found for today.")
        except Exception as e:
            speak("There was an error getting the news.")
            print("News error:", e)
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Aura....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "nexa":
                speak("Ya")
                with sr.Microphone() as source:
                    print("Aura Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
