# English-Chat-Bot
English Speaking Practice Bot

Overview
This project is a Python-based English-speaking practice bot. The bot uses the user's voice input, recognizes the speech, processes the input with an AI API, corrects any mistakes, and provides a spoken response. The bot is designed to help users improve their English language skills through conversation, providing corrections when necessary.

Features
Voice Recognition: Listens to user input through a microphone and converts it to text.
AI Response Generation: Uses an AI model to generate responses based on the conversation history.

Grammar Correction: Corrects any mistakes in the AI-generated response.

Text-to-Speech: Reads the bot's response out loud using a speech engine.

Continuous Conversation: Engages in an ongoing conversation until the user says "exit."

Requirements

Python 3.7 or higher

Internet connection (for speech recognition and API communication)


```
git clone https://github.com/Nurullah-Gelgel/English-Chat-Bot.git
cd English-Chat-Bot
```

Install Required Packages:
Make sure you have Python and pip installed. Then, install the required Python packages:
```
pip install -r requirements.txt
```

The requirements.txt file should contain:
```
speechrecognition
pyttsx3
poe-api-wrapper
asyncio
```

API Tokens:

You need to replace the tokens dictionary in the code with your actual API tokens for the Poe API.
Update the bot parameter in the fetch_response function if you are using a different AI model.

Usage
Run the Bot:
```
python english_practice_bot.py
```
Start Speaking:

After running the script, the bot will start listening for your input.
Speak clearly into the microphone.
The bot will respond after processing your input. It will also correct any mistakes and inform you of them.

Exit the Program:

To exit the program, simply say "exit."

Code Explanation

Speech Recognition: The speech_recognition library listens to your speech through the microphone and converts it into text.

AI Response Generation: The bot sends your input to an AI API to generate a response.

Correction Functionality: The correct_mistakes function demonstrates a simple way to correct mistakes in the response.

Text-to-Speech: The pyttsx3 library converts the bot's response back into speech and plays it through your speakers.