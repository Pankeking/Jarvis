import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser
import subprocess
import datetime
from fuzzywuzzy import fuzz
from phrases import CONFIRMATION_PHRASES, COMMAND_PHRASES, WAKE_UP_PHRASES
from helpers import format_date

# TODO brightness command
# TODO Date / hour command
# TODO Google commands
# TODO Structure project / Encapsulate
# TODO Make program into class and instantiates


KILL_PHRASE = "end program"

LISTEN_TIMEOUT = 2

# Initialize text-to-speech and speech-recognizer
tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.5  # Set a lower pause threshold (in seconds)
tts_engine.setProperty('rate', 180)

class Jarvis:
    def __init__(self):
        # Initialize speech recognition and reduce pause threshold
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.5
        # Initialize text to speech engine and reduce speed rate
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        # Listening status
        self.is_awake = False

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def jarvis_wake_up(self):
        # Listen for starting point
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                start_command = recognizer.listen(source, timeout=LISTEN_TIMEOUT)
                recognized_start = recognizer.recognize_google(start_command).lower()
                print(recognized_start)
                # Check activation command
                for phrase in WAKE_UP_PHRASES:
                    if phrase.lower() in recognized_start:
                        self.speak("What do you want me to do sir?")
                        self.is_awake = True
            except sr.WaitTimeoutError as e:
                # Timeout ocurred, continue waiting for wake-up phrase
                pass
            except sr.UnknownValueError as e:
                # No recognized speech, continue waiting for wake-up phrase
                pass
            except sr.RequestError as e:
                # Error with the speech recognition service, continue waiting for the wake-up phrase
                self.speak(e)

    def listen_for_commands(self):
        is_listening = False
        # Run the app continuosly
        while True:
            if not is_listening:
                is_listening = self.jarvis_wake_up()
                # if KILL_PHRASE.lower() in recognized_start.lower():
                #   speak("I believe your intentions to be hostile")
                #   return 0
            elif is_listening:
                try:
                    # Use default microphone as source
                    with sr.Microphone() as source:
                        self.speak("Listening for commands")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=LISTEN_TIMEOUT)
                    # Using Google for online recognition
                    recognized_audio = recognizer.recognize_google(audio)
                    print("You said: ", recognized_audio)
                    # Check for recognized commands and confirm before executing
                    executed = False
                    for command, phrases in COMMAND_PHRASES.items():
                        for phrase in phrases:
                            if phrase.lower() in recognized_audio.lower():
                                self.execute_command(command)
                                executed = True
                                self.speak("Waiting for the next command")
                                break
                        if executed == True:
                            break
                    if executed == False:
                        self.speak("Command not executed.")
                    print("done?")
                except sr.WaitTimeoutError as e:
                    print("No speech detected, waiting for a command")
                except sr.UnknownValueError as e:
                    print("Could not understand: ", e)
                except sr.RequestError as e:
                    print("Service Error: ", e)

    def execute_command(self, command):
        if command == "open discord":
            self.open_discord()
        elif command == "open browser":
            self.open_browser()
        elif command == "open visual studio code":
            self.open_visual_studio()
        elif command == "enter the matrix":
            self.open_terminal()
        elif command == "get date":
            self.get_date()
        elif command == "get time":
            self.get_time()
        elif command == "google this":
            self.google_this()
        elif command == "execute order 66":
            self.order_66()
        elif command == "exit the matrix":
            self.exit_matrix()

    def open_browser(self):
        self.speak("Opening default web browser")
        webbrowser.open_new_tab("http://") # Empty tab opening default user's homepage
        print("opened browser")

    def google_this(self, query):
        self.speak(f"Googling {query}")
        search_url = (f"https://www.google.com/search?={query}")
        webbrowser.open(search_url)

    def open_discord(self):
        self.speak("Opening Discord")
        subprocess.Popen("Discord", shell=True)

    def open_terminal(self):
        self.speak("Connecting to the MATRIX")
        command = "xterm -fullscreen -e cmatrix"
        subprocess.Popen(command, shell=True)

    def open_visual_studio(self):
        self.speak("Opening Visual Studio Code")
        os.system("code")

    def get_date(self):
        current_date = datetime.date.today()
        formatted_date = format_date(current_date)
        self.speak(f"La fecha es: {formatted_date}")

    def get_time(self):
        self.speak("The time is now")

    def order_66(self):
        self.speak("You were the chosen one! It was said that you would destroy the Sith, not join them! Bring balance to the Force, not leave it in darkness!")
        sys.exit()

    def exit_matrix(self):
        # Get the PID of the cmatrix process using pgrep
        process = subprocess.Popen(["pgrep", "cmatrix"], stdout=subprocess.PIPE, text=True)
        pid, _ = process.communicate()
        # Terminate the cmatrix process using kill
        if pid.strip().isdigit():
            subprocess.run(["kill", pid.strip()])
        self.speak("You have returned to Zion my child")


if __name__ == "__main__":
    assistant = Jarvis()
    while True:
        if not assistant.is_awake:
            assistant.jarvis_wake_up()
        else:
            assistant.listen_for_commands()
            

