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
