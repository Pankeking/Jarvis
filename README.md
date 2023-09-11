# Jarvis - Voice-Controlled Desktop Assistant

## Overview
**Jarvis** is a Python-based desktop assistant that allows you to control your computer using voice commands. It can perform various tasks such as opening applications, searching the web, and providing information about the date and time.

## Features
- Voice recognition: Jarvis uses the SpeechRecognition library to listen for voice commands.
- Text-to-speech: It uses the pyttsx3 library to provide spoken responses.
- Command execution: Jarvis executes commands based on recognized voice commands.
- Customizable: You can extend Jarvis by adding more command phrases and actions.
- Wake-up command: Jarvis listens for a specific wake-up phrase before accepting commands.

## Dependencies
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): For speech recognition.
- [pyttsx3](https://pypi.org/project/pyttsx3/): For text-to-speech.
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/): For fuzzy text matching.

## Usage
1. Run the Jarvis script in a Python environment.

2. Jarvis will listen for a wake-up phrase. When it hears the wake-up phrase, it becomes active and ready to accept commands.

3. Speak recognized command phrases to Jarvis, and it will execute the corresponding actions.

4. To end Jarvis, say the "end program" command.

## Voice Commands
Jarvis responds to the following voice commands:

- "Open Discord": Opens the Discord application.
- "Open browser": Opens the default web browser.
- "Open Visual Studio Code": Opens Visual Studio Code.
- "Enter the matrix": Opens a terminal with the cmatrix animation.
- "Get date": Provides the current date.
- "Get time": Provides the current time.
- "Google this": Performs a Google search based on the query.
- "Execute order 66": Quotes a famous line from Star Wars and exits the program.
- "Exit the matrix": Stops the cmatrix animation and returns to the main menu.

## Customization
You can customize Jarvis by adding more command phrases and actions. To do this:

1. Edit the `COMMAND_PHRASES` dictionary in the script.
2. Add new command phrases as keys and associate them with corresponding actions as values.

## Troubleshooting
- If Jarvis is not recognizing your voice commands, check your microphone and audio settings.
- Ensure that all dependencies are installed.

## Future Enhancements
- Implement additional commands and features.
- Improve the user interface.
- Make the program into a class and encapsulate functionality.

## License
This project is distributed under the [MIT License](LICENSE).
