import speech_recognition as sr
import pyautogui

def open_voice_access():
    pyautogui.press("win")
    pyautogui.typewrite("voice access")
    pyautogui.press("enter")
    pyautogui.press("f11")
    

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        if "activate voice control" in command:
            open_voice_access()
        else:
            print("Command not recognized")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))

if __name__ == "__main__":
    
    while True:
        listen_for_command()
