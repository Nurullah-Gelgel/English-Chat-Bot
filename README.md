# English-Chat-Bot
English Speaking Practice Bot

Overview
This project is a Python-based English-speaking practice bot designed to enhance users' English language skills through interactive conversations. The bot utilizes voice recognition to capture user speech, processes the input using an AI API, and provides spoken feedback with corrections when necessary. It's an excellent tool for practicing English speaking and improving grammar in real-time.

Features
Voice Recognition: Listens to user input through a microphone and converts spoken words into text.
AI Response Generation: Uses an AI model to generate contextually relevant responses based on the conversation history.
Grammar Correction: Automatically detects and corrects mistakes in user inputs and AI-generated responses, providing suggestions for improvement.
Text-to-Speech: Converts the bot's textual responses into spoken words using a speech engine, allowing for a fully interactive experience.
Continuous Conversation: Maintains an ongoing dialogue with the user until they say "exit," providing a fluid and engaging conversation experience.
Personalized Feedback: Provides context-aware corrections and suggestions based on user input and progress.

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

How to get your Token

Getting p-b and p-lat cookies (required)
Sign in at https://poe.com/

F12 for Devtools (Right-click + Inspect)

Chromium: Devtools > Application > Cookies > poe.com
Firefox: Devtools > Storage > Cookies
Safari: Devtools > Storage > Cookies
Copy the values of p-b and p-lat cookies

Getting formkey (optional)
Important

By default, poe-api-wrapper will automatically retrieve formkey for you. If it doesn't work, please pass this token manually by following these steps:

There are two ways to get formkey:

F12 for Devtools (Right-click + Inspect)

1st Method: Devtools > Network > gql_POST > Headers > Poe-Formkey

Copy the value of Poe-Formkey

2nd Method: Devtools > Console > Type: allow pasting > Paste this script: window.ereNdsRqhp2Rd3LEW()

Copy the result

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