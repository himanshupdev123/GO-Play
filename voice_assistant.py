import json
import pyaudio
from vosk import Model, KaldiRecognizer
import pyautogui
import pygetwindow as gw
import time
import sys
import os
import keyboard  

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Fallback to the exact directory where THIS python script lives
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
def focus_lecture_window():
    """Brings the GoClasses browser tab to the front."""
    target_keywords = ["GoClasses", "GO Classes", "Linear Algebra", "Machine Learning", "Aptitude", "Algorithms", "Python Programming", "Database Management", "Artificial Intelligence", "Calculus", "Probability and Statistics", "Theory of Computation", "Engineering Mathematics", "Discrete Mathematics", "C Programming", "Operating Systems", "Data Structures", "Computer Organization", "Digital Logic", "Computer Networks", "Compiler Design", "General Sessions"]
    
    for title in gw.getAllTitles():
        if title.strip() and any(keyword.lower() in title.lower() for keyword in target_keywords):
            try:
                win = gw.getWindowsWithTitle(title)[0]
                if win.isMinimized: win.restore()
                pyautogui.press('alt')
                time.sleep(0.1) 
                win.activate()
                print(f"👀 Successfully switched to: {title}") 
                time.sleep(0.5) 
                pyautogui.press('esc')
                return True
            except Exception as e:
                print(f"⚠️ Focus blocked: {e}")
    print("❌ Could not find any browser window!")
    return False

def get_best_microphone(p):
    """Automatically finds the best microphone index."""
    best_index = None
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        name = dev.get('name', '').lower()
        if dev.get('maxInputChannels', 0) > 0:
            if "usb" in name:
                print(f"✅ Found USB Microphone: {dev.get('name')}")
                return i
            if "array" in name or "realtek" in name:
                best_index = i
                
    if best_index is not None:
        print(f"✅ Found Built-in Microphone: {p.get_device_info_by_index(best_index).get('name')}")
        return best_index
    
    print("⚠️ No specific mic found, using default (Index 0)")
    return 0

def lecture_assistant():
    # 1. Get the path
    model_dir = resource_path("model")
    
    # 2. Print exactly where it's looking!
    print(f"🔎 DEBUG: Looking for model folder at -> {model_dir}")
    
    # 3. Check if it exists
    if not os.path.exists(model_dir):
        print("❌ Error: Could not find the 'model' folder.")
        sys.exit(1)

    print("\n==============================")
    print("   GO Play - v1.0.0          ")
    print("   Optimized for GO Classes  ")
    print("==============================")
    print("⏳ Loading offline AI model...")
    model = Model(model_dir)
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    mic_index = get_best_microphone(p)

    try:
        # Try opening the "best" found microphone
        stream = p.open(
            format=pyaudio.paInt16, 
            channels=1, 
            rate=16000, 
            input=True, 
            frames_per_buffer=8000, 
            input_device_index=mic_index
        )
    except Exception as e:
        print(f"⚠️ Error opening mic {mic_index}: {e}")
        print("🔄 Attempting to use default system microphone...")
        # Fallback: Try opening the default device (no index specified)
        try:
            stream = p.open(
                format=pyaudio.paInt16, 
                channels=1, 
                rate=16000, 
                input=True, 
                frames_per_buffer=8000
            )
        except Exception as final_e:
            print(f"❌ Critical Error: Could not open any audio device. {final_e}")
            sys.exit(1)

    stream.start_stream()

    print("\n🎙️ Smart Lecture Assistant Started.")
    print("Commands: 'Ok sir', 'Ok mam', 'Repeat that'")
    
    cooldown_until = 0 

    try:
        while True:
            # ---> ADD THIS NEW BLOCK <---
            # If you press Ctrl+Alt+Q anywhere on your computer, the app instantly dies.
            if keyboard.is_pressed('ctrl+alt+q'):
                os._exit(0)
            data = stream.read(4000, exception_on_overflow=False)
            
            if time.time() < cooldown_until:
                continue
            
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
            else:
                partial = json.loads(recognizer.PartialResult())
                text = partial.get("partial", "")

            if not text:
                continue

            print(f"🤖 AI Hearing: '{text}'")

            # Logical Triggers
            if any(phrase in text for phrase in ["ok sir", "okay sir", "ok sar", "okay sar", "ok mam", "okay mam","done sir", "done mam","done","dancer","okay so","okay said","go stop","go play","goblin","god bless","good play","stop","play"]):
                print("⏸️/▶️ Play/Pause Triggered!")
                focus_lecture_window()
                pyautogui.press('space') 
                recognizer.Reset()
                cooldown_until = time.time() + 2.0 

            elif any(phrase in text for phrase in ["didn't understand", "repeat that", "go back","back"]):
                print("⏪ Rewind Triggered!")
                focus_lecture_window()
                pyautogui.press('left')
                pyautogui.press('left')
                recognizer.Reset()
                cooldown_until = time.time() + 2.0 

    except KeyboardInterrupt:
        print("\nExiting. Happy studying!")
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    lecture_assistant() 