# TSA PROJECT - Jarvis Personal Assistant
import subprocess
import sys

# Automatically install ALL the libraries
'''
libraries = ['SpeechRecognition', 'pyttsx3', 'PyAudio', 'wikipedia', 'ollama']
cmd = 'pip install '
num = 0
for lib in libraries:
    subprocess.run(cmd + libraries[num])
    num += 1
'''

# Auto install the missing libraries
dependencies = {
    'SpeechRecognition': 'speech_recognition',
    'pyttsx3': 'pyttsx3',
    'PyAudio': 'pyaudio',
    'wikipedia': 'wikipedia',
    'ollama': 'ollama'
}

for package, module in dependencies.items():
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.run([sys.executable, "-m", "pip", "install", package])

# Standard Imports -----------------------------------------------------------
try:
    import speech_recognition as sr
except ImportError:
    sr = None
    print("Warning: speech_recognition not found.")

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None
    print("Warning: pyttsx3 not found.")

import webbrowser
import datetime
import wikipedia
import os
from ollama import chat

# Speak function --------------------------------------------
def speak(audio):
    if pyttsx3 is None:
        # Print output instead if no voice is present
        print(f"[Jarvis]: {audio}")
        return
    
    engine = pyttsx3.init()
    # Set  voice (0 for male, 1 for female)
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id) 
    
    engine.say(audio)
    engine.runAndWait()

# Listen function --------------------------------------
def listen():
    if sr is None:
        print("Voice input is disabled (Library missing).")
        return ""
        
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1 
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        # Google's speech recognition stuff
        command = recognizer.recognize_google(audio, language='en-us') 
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand audio. Please repeat.")
        return ""
        
    return command.lower()

# Typing Input function -------------------------------------------------------
def typed():
    command = input("Please type your command: ")
    return command.lower()

# Commands (Functions) -------------------------------
def tell_time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {time}")

def ollama_call(command):
    # Let the person know ollama is processing
    print("[System] Sending request to Ollama, please wait...")
    
    try:
        response = chat(
            model='gemma3:1b',
            messages=[{'role': 'user', 'content': f'{command}'}],
        )
        
        # Simple check for response format
        if hasattr(response, 'message'):
            reply = response.message.content
        else:
            reply = response['message']['content']
            
        print(f"\n[Jarvis Response]: {reply}\n")
        speak(reply)
        
    except Exception as e:
        # Error handling for connection or model issues
        print(f"\n[Error] Could not connect to Ollama: {e}\n")
        speak("I am having trouble connecting to my local brain.")

def open_website(command):
    # Removes 'open' to get the site name (like "open google" ----> "google")
    site_name = command.replace("open", "").strip()
    if site_name:
        speak(f"Opening {site_name}")
        webbrowser.open(f"https://www.{site_name}.com")

def search_wikipedia(command):
    speak('Searching the Wik...')
    query = command.replace("wikipedia search for", "").strip()
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception:
        speak("I could not find a specific Wikipedia page for that.")

# Main loop -----------------------
def main():
    speak("Hello, I am your personal assistant. How can I help you today?")
    preference = input("Would you like to talk, or type? ('talk'/'type'): ").lower()
    
    while True:
        if preference == "talk":
            command = listen()
        else:
            command = typed()
        
        if not command:
            continue
        
        # The logic/what should happen
        if 'time' in command:
            tell_time()
        elif 'open' in command:
            open_website(command)
        elif 'wikipedia' in command:
            search_wikipedia(command)
        elif 'jarvis' in command:
            ollama_call(command)
        elif 'exit' in command or 'bye' in command or 'stop' in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            # the "fallback"/regular jarvis 
            ollama_call(command)

if __name__ == "__main__":
    main()
