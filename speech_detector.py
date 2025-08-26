import speech_recognition
import gui_automation
import pyautogui

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# The gui instance will be used to call GUI functions defined by us in 'gui_automation.py'
gui = gui_automation.GuiControl()
recognizer = speech_recognition.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))
speak("voice navigation activated")
with speech_recognition.Microphone() as src:
    while True:
        
        try:
            recognizer.adjust_for_ambient_noise(src)
            print("\n\nThreshold Value After calibration:" + str(recognizer.energy_threshold))
            print("\nPlease speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio)
            # speech_to_txt = recognizer.recognize_google_cloud(audio).lower()
        except Exception as ex:
            print("Sorry. Could not understand.\n\n")
            speak("Sorry. Could not understand")
            continue

        

        print("I heard : " + speech_to_txt)

        # ---------------------------------------------------------------------
        # The following if-else block is for the commands I have chosen and
        # call their respective GUI action
        # ---------------------------------------------------------------------
        if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
            break
        elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
            gui.mouse_up(recognizer, src)
        elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
            gui.mouse_down(recognizer, src)
        elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
            gui.mouse_left(recognizer, src)
        elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
            gui.mouse_right(recognizer, src)
        elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
            gui.left_click()
        elif speech_to_txt == "right click" or speech_to_txt == "right-click":
            gui.right_click()
        elif speech_to_txt == "double click" or speech_to_txt == "double-click":
            gui.double_click()
        # elif speech_to_txt == "open telegram":
        #     gui.open_telegram()
        # elif speech_to_txt == "open notepad":
        #     gui.open_notepad()
        elif speech_to_txt == "mute" or speech_to_txt == "unmute":
            gui.mute_unmute()
        elif speech_to_txt == "play" or speech_to_txt == "pause":
            gui.play_pause()
        elif speech_to_txt == "volume up" or speech_to_txt == "sound up":
            gui.volume_up()
        elif speech_to_txt == "volume down" or speech_to_txt == "sound down":
            gui.volume_down()
        elif speech_to_txt== "click student":
            try:
                gui.click_student(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click email":
            try:
                gui.click_email(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt == "type email":
            gui.email_typing()
        elif speech_to_txt == "start typing":
            gui.voice_typing()
        elif speech_to_txt== "click password":
            try:
                gui.click_password(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click login":
            try:
                gui.click_login(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click register":
            try:
                gui.click_register(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click go back":
            try:
                gui.click_goback(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click ok":
            try:
                gui.click_ok(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click go to exam":
            try:
                gui.click_gotoexam(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click start exam":
            try:
                gui.click_startexam(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt == "start scrolling":
            gui.voice_scroll()
        elif speech_to_txt== "click submit exam":
            try:
                gui.click_submitexam(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click logout":
            try:
                gui.click_logout(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click my result":
            try:
                gui.click_myResult(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        elif speech_to_txt== "click subject":
            try:
                gui.click_subject(recognizer, src)
        
            except pyautogui.ImageNotFoundException:
                print("Image not found. Continuing listening for commands.")
                continue
        

    