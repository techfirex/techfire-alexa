#Required Modules
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import random
import smtplib
import datetime
import wikipedia
import pywhatkit
import pyjokes
import operator

# Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Python Text-to-Speech (pyttsx3)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)

# Wake word in Listen Function // like ok google
WAKE = "techfire"

# Used to store user commands for analysis
CONVERSATION_LOG = "Conversation Log.txt"

# Initial analysis of words that would typically require a Google search
SEARCH_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}

# class techfire
# function hear-->input/command, speak-->output/responce, listen-->wake_word, start_conversation_log, remember_conversation_log, open_things, understanding_time, get_weather, perform_maths, analyze-->command analyse and call func

class Techfire:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def hear(self, recognizer, microphone):
        try:
            with microphone as source:
                print("Hearing...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                recognizer.pause_threshold = 1
                # recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                t.remember_conversation_log(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")

    def listen(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    recognizer.pause_threshold = 1
                    # recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source)
                    response = recognizer.recognize_google(audio)

                    if response == WAKE:
                        t.speak("How can I help you?")
                        return response.lower()

                    else:
                        pass

            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error.")

    def open_something(self, command):
        if command == "open youtube":
            t.speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")

        elif command == "open facebook":
            t.speak("Opening Facebook.")
            webbrowser.open("https://www.facebook.com")
        
        elif command == "open google":
            t.speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        else:
            t.speak("I don't know how to open that yet.")

    def start_conversation_log(self):
        today = str(datetime.date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as file:
            file.write("CONVERSATION STARTED ON: " + today + "\n")

    def remember_conversation_log(self, command):
        with open(CONVERSATION_LOG, "a") as file:
            file.write("USER: " + command + "\n")

    def analyze(self, command):
        try:
            if command.startswith('open'):
                self.open_something(command)
            
            elif command == "introduce yourself" or "who are you":
                t.speak("I am Techfire. I'm a digital assistant.")

            elif command == "how are you":
                current_feelings = ["I'm fine.", "Very happy.", "I am okay.", "Scared"]
                greeting = random.choice(current_feelings)
                t.speak(greeting)

            elif SEARCH_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:
                self.search_words(command)

            else:
                t.speak("I don't know how to do that yet.")

        except TypeError:
            print("Warning: You're getting a TypeError somewhere.")

        except AttributeError:
            print("Warning: You're getting an Attribute Error somewhere.")

    def search_words(self, command):
        t.speak("Here is what I found.")
        webbrowser.open("https://www.google.com/search?q={}".format(command))

t = Techfire()
t.start_conversation_log()
previous_response = ""
while True:
    response = t.listen(recognizer, microphone)
    command = t.hear(recognizer, microphone)

    if command == previous_response:
        t.speak("You already asked that. Ask again if you want to do that again.")
        previous_command = ""
        response = t.listen(recognizer, microphone)
        command = t.hear(recognizer, microphone)

    t.analyze(command)
    previous_response = command