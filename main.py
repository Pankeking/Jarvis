import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser
import subprocess
from fuzzywuzzy import fuzz
from phrases import CONFIRMATION_PHRASES, COMMAND_PHRASES, WAKE_UP_PHRASES

# TODO brightness command
# TODO Date / hour command
# TODO Google commands
# TODO Structure project / Encapsulate


KILL_PHRASE = "end program"

LISTEN_TIMEOUT = 3

# Initialize text-to-speech and speech-recognizer
tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def confirm_action(action):
    # Initialize Voice Recognition
    recognizer = sr.Recognizer()
    speak(f"Do you want to {action}")
    with sr.Microphone() as source:
        print("waiting confirmation")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio_confirmation = recognizer.listen(source)
            text_confirmation = recognizer.recognize_google(audio_confirmation)
            print(text_confirmation)
            # Check positive response from confirmation phrases
            for phrase in CONFIRMATION_PHRASES:
                if phrase.lower() in text_confirmation.lower():
                    return True
            return False
        except sr.WaitTimeoutError as e:
            print(e)
        except sr.RequestError as e:
            print(e)
        except sr.UnknownValueError as e:
            print(e)

def jarvis_wake_up():
    print("Suspended, awaiting")
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
                    speak("What do you want me to do sir?")
                    return True
        except sr.WaitTimeoutError as e:
            # Timeout ocurred, continue waiting for wake-up phrase
            pass
        except sr.UnknownValueError as e:
            # No recognized speech, continue waiting for wake-up phrase
            pass
        except sr.RequestError as e:
            # Error with the speech recognition service, continue waiting for the wake-up phrase
            speak(e)
            return False

def listen_for_commands():
    is_listening = False
    # Run the app continuosly
    while True:
        if not is_listening:
            is_listening = jarvis_wake_up()
            # if KILL_PHRASE.lower() in recognized_start.lower():
            #   speak("I believe your intentions to be hostile")
            #   return 0
        elif is_listening:
            print("listening")
            try:
                # Use default microphone as source
                with sr.Microphone() as source:
                    print("Listening for commands")
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
                            if confirm_action(command):
                                execute_command(command)
                                executed = True
                                break
                            else:
                                speak("Command not executed.")
                        if executed == True:
                            break
                print("done?")
            except sr.WaitTimeoutError as e:
                print("No speech detected, waiting for WAKE-UP phrase")
            except sr.UnknownValueError as e:
                print("Could not understand: ", e)
            except sr.RequestError as e:
                print("Service Error: ", e)

def execute_command(command):
    if command == "open discord":
        open_discord()
    elif command == "open browser":
        open_browser()
    elif command == "open visual studio code":
        open_visual_studio()
    elif command == "enter the matrix":
        open_terminal()
    elif command == "get date":
        get_date()
    elif command == "get time":
        get_time()
    elif command == "google this":
        google_this()
    elif command == "execute order 66":
        order_66()
    elif command == "exit the matrix":
        exit_matrix()

def open_browser():
    speak("Opening default web browser")
    webbrowser.open_new_tab("http://") # Empty tab opening default user's homepage
    print("opened browser")

def google_this(query):
    speak(f"Googling {query}")
    search_url = (f"https://www.google.com/search?={query}")
    webbrowser.open(search_url)

def open_discord():
    speak("Opening Discord")
    os.system("Discord")

def open_terminal():
    speak("Connecting to the MATRIX")
    command = "xterm -fullscreen -e cmatrix"
    subprocess.Popen(command, shell=True)

def open_visual_studio():
    speak("Opening Visual Studio Code")
    os.system("code")

def get_date():
    speak("The date is today")

def get_time():
    speak("The time is now")

def order_66():
    speak("You were the chosen one! It was said that you would destroy the Sith, not join them! Bring balance to the Force, not leave it in darkness!")
    sys.exit()

def exit_matrix():
    # Get the PID of the cmatrix process using pgrep
    process = subprocess.Popen(["pgrep", "cmatrix"], stdout=subprocess.PIPE, text=True)
    pid, _ = process.communicate()
    # Terminate the cmatrix process using kill
    if pid.strip().isdigit():
        subprocess.run(["kill", pid.strip()])
    speak("You have returned to Zion my child")


def main():
    listen_for_commands()

if __name__ == "__main__":
    main()

