import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input through voice."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Network error. Please check your internet connection."

if __name__ == "__main__":
    speak("Waiting for the instruction...")
    while True:
        print("Provide me the instruction loudly")
        user_command = listen()

        if "turn left" in user_command: 
            speak("Turning left")
        
        if "turn right" in user_command: 
            speak("Turning right")

        if "come to base" in user_command: 
            speak("Coming to base")

        if "take off" in user_command: 
            speak("taking off")

        if "activate emergency mode" in user_command: 
            speak("activating emergency mode")

        elif "exit" in user_command or "quit" in user_command:
            speak("Goodbye! Have a good Day")
            break
        
        else:
            print(f"You said: {user_command}")
