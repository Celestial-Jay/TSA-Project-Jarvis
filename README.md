# Jarvis - Accessibility Assistant
TSA Software Development 2026 | Oklahoma State Conference
By: Jayden Tsiambom & Yejun Choi 

---

## Overview

Jarvis is a voice personal assistant built to reduce the accessibility barrier for people with visual or hearing disabilities. Users can interact with their computer entirely through natural speech, so no mouse or keyboard required. A text input option is also available for users who prefer or need it.

---

## Features

- Speaks the current time when asked
- Opens websites by name ("open youtube")
- Searches and reads Wikipedia summaries
- Answers general questions using a locally-run AI model (Ollama / Gemma 4)
- All responses are spoken aloud via text-to-speech

---

## Technologies Used

- `SpeechRecognition` — converts spoken audio to text via Google's API
- `pyttsx3` — offline text-to-speech engine
- `PyAudio` — microphone input
- `Ollama` with `gemma4:e2b` — local AI model for general question answering
- `wikipedia` — article summarization
- `webbrowser` / `datetime` — built-in Python standard library utilities

---

## How to Run

Prerequisites: Python 3.9+, and [Ollama](https://ollama.com) installed and running locally with the gemma4:e2b model pulled.

```bash
ollama pull gemma4:e2b
```

```bash
git clone https://github.com/Celestial-Jay/TSA-Project-Jarvis.git
cd TSA-Project-Jarvis
pip install SpeechRecognition pyttsx3 PyAudio wikipedia ollama
python jarvis.py
```

On startup, choose `talk` for voice input or `type` for keyboard input, then speak or type commands normally.

Note for judges: A full live demonstration will be provided at the state conference. All required hardware and software will be supplied by us so you don't have to install anything.
