# 🎙️ GO Play - Smart Lecture Assistant Optimised for GOClasses

**GO Play** is an offline, AI-powered voice assistant built specifically for students of GOClasses. It allows you to control video playback completely hands-free using voice commands, so you can focus 100% on taking handwritten notes.

⚠️ **IMPORTANT COMPATIBILITY NOTE:** This application is specifically optimized for **laptops** and is exclusively designed to work with **GO Classes** course videos.

## ✨ Features
* **100% Offline:** Uses the Vosk AI model to process speech locally. No internet required, no privacy concerns.
* **Invisible Execution:** Runs completely in the background with a zero-footprint UI so it doesn't clutter your screen.
* **Smart Audio Routing:** Automatically detects external USB microphones or falls back to your built-in laptop mic.

## 🚀 How to Use (Read Carefully)
Because this app runs silently in the background, please follow these exact steps for it to work perfectly:

1. **Launch the App:** Double-click the `GO Play.exe` file. **There is no console or pop-up window.** Simply wait for about **3 seconds** for the AI to load silently in the background.
2. **Focus the Tab:** Open your web browser and go to your GO Classes lecture. You **must** click inside the tab where the video is playing. *(Note: If you are clicked into a different window, tab, or application, the voice commands will not work).*
3. **Wait for Silence:** To ensure the AI hears you perfectly, **do not give commands while the instructor is speaking**. Wait for a natural pause or a moment of silence so there is no ambiguity between the lecture audio and your voice.

## 🗣️ Voice Commands
Speak clearly into your laptop mic or headphones:
* "Ok Sir"/"Go Play" -> **Play/Pause** the lecture.
* `"Repeat that"` / `"Didn't understand"` -> **Rewinds** the video by 10 seconds.
* `"Done sir"`/"Go Stop"/"Done" -> **Resumes** playback after you finish writing.

## 🛑 How to Stop the App
Since the app runs invisibly in the background, you cannot close it with an "X" button. 
* To completely shut down the application at any time, press **`Ctrl + Alt + Q`** on your keyboard, or simply say **"Close assistant"**.

## 📥 Installation
1. Go to the [Releases page](../../releases) and download the latest `GO Play.exe`.
2. Save it to your desktop or a study folder.
3. Put on your headphones and start studying!

## 🤝 For Developers & Contributors
Want to add new features, like Mac support or new voice commands? We'd love your help! 

### Local Setup Instructions
1. **Fork & Clone:** Fork this repository and clone it to your local machine.
2. **Virtual Environment:** Create a fresh Python environment so you don't clutter your system:
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows

Install Dependencies: Install all required libraries in one go:
 ```bash
pip install -r requirements.txt

Test the Code: You don't need to build the .exe to test your changes. Just run the raw Python script:
 ```bash
python voice_assistant.py

Gemini said
That is exactly the mindset of a great open-source developer! Thinking about how other programmers will interact with your code is what takes a project to the next level.

To answer your question: Yes, you absolutely need a requirements.txt file. When another student downloads your raw Python code, their computer won't know which libraries you used. If they just try to run voice_assistant.py, their terminal will light up with red "ModuleNotFoundError" messages. The requirements.txt acts as a grocery list so they can install everything in one click.

Here is how to set up your repo for collaborators, starting with that file.

Step 1: Create the requirements.txt
You can either ask Python to generate this automatically, or just create a new text file named requirements.txt in your project folder and paste this clean list into it:

Plaintext
vosk==0.3.45
PyAudio==0.2.14
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
keyboard==0.13.5
pyinstaller==6.4.0
(Note: I included keyboard assuming you added that Ctrl+Alt+Q kill switch!)

Step 2: Add "For Developers" instructions to the README
Contributors need to know how to test the code without compiling it into an .exe every single time.

Add this new section to the bottom of your README.md file:

Markdown
## 🤝 For Developers & Contributors
Want to add new features, like Mac support or new voice commands? We'd love your help! 

### Local Setup Instructions
1. **Fork & Clone:** Fork this repository and clone it to your local machine.
2. **Virtual Environment:** Create a fresh Python environment so you don't clutter your system:
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
Install Dependencies: Install all required libraries in one go:

Bash
pip install -r requirements.txt
Test the Code: You don't need to build the .exe to test your changes. Just run the raw Python script:

Bash
python voice_assistant.py
How to Contribute
Create a new branch for your feature (git checkout -b feature/NewCommand).

Commit your changes.

Push to the branch and open a Pull Request. Please describe exactly what your code changes or fixes!


