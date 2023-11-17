# from typing import Text
import speech_recognition as sr
from selenium import webdriver
import pyttsx3
import pywhatkit
import pyjokes
import webbrowser
from datetime import date
import os
import sys
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def takeCommand():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)    
    try:
        print("Recognizing...") 
        text = r.recognize_google(audio)
        print(f"You Said: {text}\n")
        text = text.lower()
    except: 
        print("say something...!")
        return "None"
    return text

def run_techfire():
    text = takeCommand()
    remember(text)
    if 'play' in text:
        song = text.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'joke' in text:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    
    elif "open google" in text:
        speak("opening google.")
        webbrowser.open("https://www.google.com")

    elif "open download" in text:
        speak("opening download folder")
        download = get_download_folder()
        os.startfile(download)
    
    elif "open desktop" in text:
        speak("opening desktop folder")
        desktop = get_desktop_folder()
        os.startfile(desktop)

    elif "open my gmail account" in text:
        try:
            speak("opening gmail and logging in")
            driver = webdriver.Chrome(executable_path=r"C:\Users\tushar\Downloads\chromedriver_win32\chromedriver.exe")
            driver.get("http://gmail.com")
            time.sleep(5)
            driver.find_element_by_id("identifierId").send_keys('################@gmail.com')
            time.sleep(2)
            driver.find_element_by_id("identifierNext").click()
            time.sleep(5)
            driver.find_element_by_name("password").send_keys('##############')
            time.sleep(2)
            driver.find_element_by_id("passwordNext").click()
        except:
            pass
    
    elif "exit" in text:
        speak("exiting..!, see you soon")
        sys.exit()

    else:
        pass

def start_conversation_log():
        today = str(date.today())
        today = today
        with open("Conversation Log.txt", "a") as f:
            f.write("Conversation started on: " + today + "\n")
        
def remember(command):
        with open("Conversation Log.txt", "a") as f:
            if command != "None":
                f.write("User: " + command + "\n")

def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")

def get_desktop_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Desktop")

start_conversation_log()
while True:
    run_techfire()