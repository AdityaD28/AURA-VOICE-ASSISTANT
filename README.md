#  Ara: AI-Powered Voice Assistant using Python

**Aura** is a smart, voice-activated virtual assistant built using Python. Think of it as your personal desktop AI — capable of responding to voice commands, answering general questions via GPT, playing music, fetching weather updates, reading the latest news, and opening popular websites. Inspired by virtual assistants like **Alexa**, **Siri**, and **Google Assistant**, Nexa brings AI-powered interaction to your terminal.

---

##  What Can Aura Do?

-  Voice-activated hotword detection ("Aura")
-  Answer your questions using ChatGPT (GPT-3.5 Turbo)
-  Search summaries from Wikipedia
-  Play music using a YouTube-based music library
-  Get current weather updates from any city
-  Fetch the latest news headlines (from India)
-  Open common websites like Google, YouTube, LinkedIn, etc.
-  Tell you the current time and date

---

##  Tech Stack

| Category           | Tool/Library Used            |
|-------------------|------------------------------|
| Voice Input        | `speech_recognition`         |
| Text-to-Speech     | `gTTS`, `pyttsx3`, `pygame`  |
| AI Responses       | `openai` (ChatGPT)           |
| Music Search       | `fuzzywuzzy` (string match)  |
| Web Data           | `wikipedia`, `requests`      |
| News API           | `NewsAPI.org`                |
| Weather API        | `OpenWeatherMap`             |
| Browser Automation | `webbrowser`                 |

---

##  Project Structure

```
nexa-voice-assistant/
├── main.py             # Core logic of Nexa assistant
├── client.py           # Standalone ChatGPT test client
├── musicLibrary.py     # Custom music-to-YouTube mapping
├── requirements.txt    # Python dependencies
└── README.md           # You're here!
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/aura-voice-assistant.git
cd aura-voice-assistant
```
### 2. Install Required Dependencies

Install all dependencies using pip:
```bash
pip install -r requirements.txt
```
### 3. Add Your API Keys
Open main.py and client.py and update the placeholders:
```bash
# main.py
newsapi = "your_newsapi_key_here"
OpenAI(api_key="your_openai_api_key_here")
api_key = "your_openweathermap_key_here"

# client.py
client = OpenAI(api_key="your_openai_api_key_here")
```
## How to Run

### 1. Run the Main Script
```bash
python main.py
```
### 2. Say the Hotword
Wait until you see:
```bash
Listening...
```
Say:
```bash
Aura
```
The assistant will respond with:
```bash
Ya
```
Now you're in command mode. Speak your command. Examples:

- "What is Machine Learning?"

- "Play Skyfall"

- "Weather in Bangalore"

- "News"

- "Open YouTube"

- "What is Python?"

## Example Voice Commands

| Command             | What Happens                            |
| ------------------- | --------------------------------------- |
| "Open Google"       | Launches Google in your browser         |
| "Play Skyfall"      | Opens corresponding YouTube song        |
| "Weather in Mumbai" | Fetches weather from OpenWeatherMap     |
| "News"              | Reads latest 5 headlines from NewsAPI   |
| "What is AI?"       | Answers using Wikipedia or GPT fallback |
| "Time" / "Date"     | Announces current time or date          |

## Custom Music Library
The music library is in musicLibrary.py. Add your favorite tracks like this:
```bash
music = {
    "skyfall": "https://youtube.com/your-skyfall-link",
    "stealth": "https://youtube.com/your-stealth-link"
}
```
## API Key Security(Optional but highly recommended)
To keep your keys safe, do this:
### 1. Install python-dotenv:
```bash
pip install python-dotenv
```
### 2. Create a .env file in your root folder:
```bash
OPENAI_API_KEY=your_openai_key
NEWS_API_KEY=your_newsapi_key
WEATHER_API_KEY=your_openweathermap_key
```
### 3. In your code, update API key loading:
```bash
from dotenv import load_dotenv
load_dotenv()

import os
openai_key = os.getenv("OPENAI_API_KEY")
```

## How It Works (Behind the Scenes)
1. Listening Loop: Constantly waits for the word "Aura".
2. Voice Activation: Once heard, it activates and listens again for your actual command.
3. Command Parsing: Determines intent (open site, play music, ask GPT, etc.).
4. Task Execution: Launches the relevant function:
- webbrowser.open() for URLs
- wikipedia.summary() for info
- openai.ChatCompletion for AI replies
- requests.get() for weather/news APIs

## Testing GPT Separately
You can run client.py to test if your OpenAI API key works:
```bash
python client.py
```
## Requirements
```bash
speechrecognition
pyttsx3
gtts
pygame
requests
wikipedia
fuzzywuzzy
openai
python-Levenshtein
```
Install them via:
```bash
pip install -r requirements.txt
```

## Future Improvements
- Voice wake word detection using Vosk or Snowboy

- Whisper API for improved speech-to-text accuracy

- GUI interface using Tkinter or Streamlit

- Spotify/Youtube API for dynamic music search

- Context-based conversations via AI memory

- Support for multiple languages

## Author

Developed by Aditya Dasappanavar  
GitHub: [AdityaD28](https://github.com/AdityaD28)

## License
This project is licensed under the MIT License.

You’re free to modify, distribute, and use this software with attribution.
