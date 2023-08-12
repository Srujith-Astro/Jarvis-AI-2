import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import openai
import pyttsx3
import requests

chatStr = " "


def get_news_headlines(max_headlines=3):
    API_KEY = 'bcce7e06ddfc486cbc16d94b7d83f06b'
    endpoint = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': API_KEY,
        'country': 'in',  # You can change this to the desired country code
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        headlines_read = 0  # Keep track of the number of headlines read
        for article in articles:
            if headlines_read >= max_headlines:  # Check if the maximum number of headlines has been reached
                break
            title = article['title']
            say(f"News: {title}")
            headlines_read += 1
    else:
        say('Sorry, I could not retrieve the news at the moment.')
        
def ai(query):
    global chatStr
    openai.api_key = "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"
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    openai_response = response.choices[0].text
    chatStr += f"Jarvis: {openai_response}\n"
    return openai_response

def chat(query):
    global chatStr
    if "Open music".lower() in query.lower():
        musicpath = r"C:\Users\sruji\Dropbox\My PC (LAPTOP-K0CAA86I)\Documents\Music"
        subprocess.Popen(['explorer', musicpath])
    elif "Open Brave".lower() in query.lower():
        musicpath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
        subprocess.Popen(['explorer', musicpath])
    elif "Hello Jarvis".lower() in query.lower():
        musicpath = r"C:\Users\sruji\Dropbox\My PC (LAPTOP-K0CAA86I)\Documents\2023\home\AIAA\AIAA\JARVIS TIKTOK PC SOUND FREE HIGH QUALITY  AC_DC WINDOWS STARTUP SOUND.mp4"
        subprocess.Popen(['explorer', musicpath])
    elif "time" in query:
        Hour = datetime.datetime.now().strftime("%H")
        Min = datetime.datetime.now().strftime("%M")
        say(f"Sir, the time is {Hour} gantala {Min} nimishaaalu")
    elif "news" in query.lower():
        get_news_headlines()
    elif "Using AI".lower() in query.lower():
        response = ai(query)
        say(response)
        if os.path.exists("OpenAI"):
            prompt_suffix = query.split('Using AI', 1)[1].strip() if 'Using AI' in query else query
            with open(f"OpenAI/{prompt_suffix}.txt", "w") as f:
                f.write(response)
    
                
    else:
        response = ai(query)
        say(response)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Spyder')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening")
        query = takeCommand()
        sites = [["Youtube", "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} sir........")
        if "news" in query.lower():
            get_news_headlines()
        chat(query)
