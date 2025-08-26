import pyautogui
import speech_recognition
import pyttsx3

# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER = 1000
SLOWER = 200

def backspace():
    pyautogui.press('backspace')
    print("Backspace command executed.")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


class GuiControl:
    @staticmethod
    def __init__():
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    # ------------------------------------------------------------------------------------
    # Moves the Mouse pointer UPWARDS from it's current position,
    # until 'STOP' keyword is heard.
    # ------------------------------------------------------------------------------------
    @staticmethod
    def mouse_up(recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1 * SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                pass
            print("Inside mouse up :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1 * FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1 * SLOWER, duration=0.25)

    # ------------------------------------------------------------------------------------
    # Moves the Mouse pointer DOWNWARDS from it's current position,
    # until 'STOP' keyword is heard.
    # ------------------------------------------------------------------------------------
    @staticmethod
    def mouse_down(recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1 * SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                pass
            print("Inside mouse down :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1 * FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1 * SLOWER, duration=0.25)

    # ------------------------------------------------------------------------------------
    # Moves the Mouse pointer LEFTWARD from it's current position,
    # until 'STOP' keyword is heard.
    # ------------------------------------------------------------------------------------
    @staticmethod
    def mouse_left(recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1 * SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                pass
            print("Inside mouse left :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1 * FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1 * SLOWER, 0, duration=0.25)

    # ------------------------------------------------------------------------------------
    # Moves the Mouse pointer RIGHTWARD from it's current position,
    # until 'STOP' keyword is heard.
    # ------------------------------------------------------------------------------------
    @staticmethod
    def mouse_right(recognizer, src):
        # print("Move mouse right")
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1 * SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                pass
            print("Inside mouse right :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1 * FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1 * SLOWER, 0, duration=0.25)

    # ------------------------------------------------------------------------------------
    # CLICKS the LEFT Mouse button it's current position
    # ------------------------------------------------------------------------------------
    @staticmethod
    def left_click():
        pyautogui.click()

    # ------------------------------------------------------------------------------------
    # CLICKS the RIGHT Mouse button it's current position
    # ------------------------------------------------------------------------------------
    @staticmethod
    def right_click():
        print("Right Clicking")
        pyautogui.click(button='right', clicks=2, interval=0.25)

    # ------------------------------------------------------------------------------------
    # DOUBLE CLICKS the LEFT Mouse button it's current position
    # ------------------------------------------------------------------------------------
    @staticmethod
    def double_click():
        print("Double Clicking")
        pyautogui.click(button='left', clicks=2, interval=0.25)

    # ------------------------------------------------------------------------------------
    # CLICKS the CHROME icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the
    # program is run.
    # ------------------------------------------------------------------------------------
    # @staticmethod
    # def open_telegram():
    #     print("Opening telegram")
    #     icon_location = pyautogui.locateOnScreen(r'C:\Users\Prathmesh Patil\Desktop\tele.png') # C:\Users\Prathmesh Patil\Desktop\tele.png
    #     # print(type(icon_location))
    #     if icon_location is not None:
    #         if len(icon_location) == 4:
    #             # Box(left=446, top=1023, width=74, height=52)
    #             # Calculate point x,y position to click based on above location
    #             # pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
    #             pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
    #     else:
    #         print("Could not locate telegram Icon on screen")

    # # ------------------------------------------------------------------------------------
    # # CLICKS the NOTEPAD icon (if present in taskbar)
    # # A screenshot needs to be captured and stored in 'screenshots' folder, before the
    # # program is run.
    # # ------------------------------------------------------------------------------------
    # @staticmethod
    # def open_notepad():
    #     print("Opening Notepad")
    #     icon_location = pyautogui.locateOnScreen(r'screenshots\Notepad.PNG')
    #     if icon_location is not None:
    #         if len(icon_location) == 4:
    #             # Box(left=446, top=1023, width=74, height=52)
    #             # Calculate point x,y position to click based on above location
    #             # pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
    #             pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
    #     else:
    #         print("Could not locate Notepad Icon on screen")

    # ------------------------------------------------------------------------------------
    # Simulates the MUTE/UNMUTE key press
    # ------------------------------------------------------------------------------------
    @staticmethod
    def mute_unmute():
        print("Pressing Mute/Unmute Key")
        pyautogui.typewrite(['volumemute'])

    # ------------------------------------------------------------------------------------
    # Simulates the SPACE key press
    # ------------------------------------------------------------------------------------
    @staticmethod
    def play_pause():
        print("Pressing SPACE Key")
        pyautogui.typewrite(['space'])

    # ------------------------------------------------------------------------------------
    # Simulates the VOLUME UP key press
    # ------------------------------------------------------------------------------------
    @staticmethod
    def volume_up():
        pyautogui.typewrite(['volumeup'])

    # ------------------------------------------------------------------------------------
    # Simulates the VOLUME DOWN key press
    # ------------------------------------------------------------------------------------
    @staticmethod
    def volume_down():
        pyautogui.typewrite(['volumedown'])
    
    #---------------------------------------------------------------------------------------------
    #click student
    #---------------------------------------------------------------------------------------------
    @staticmethod
    def click_student(recognizer, src):
        while True:
            speech_to_txt = ""
            stud_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_student.png", confidence=0.9 )
            pyautogui.moveTo(stud_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked student button:" + speech_to_txt)
    #---------------------------------------------------------------------------------------------
    #click email
    #---------------------------------------------------------------------------------------------

    @staticmethod
    def click_email(recognizer, src):
        while True:
            speech_to_txt = ""
            email_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_email.png", confidence=0.8 )
            pyautogui.moveTo(email_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked email button:" + speech_to_txt)
    
    @staticmethod
    def email_typing():
        
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            try:
                    speak("started email typing")
                    while True:
                        audio = recognizer.listen(source, timeout=None)
                        
                        try:
                            text = recognizer.recognize_google(audio).lower()
                            if "stop typing" in text:
                                print("Stopping voice typing.")
                                speak("exiting email typing")
                                break
                            elif "at the rate" in text:
                                email = text.replace(" at the rate ", "@").replace(" ", "")
                                print(f"Typed: {email}")
                                pyautogui.typewrite(email)
                            else:
                                print("Sorry, I can only type email addresses. Please try again.")
                        except speech_recognition.UnknownValueError:
                            continue
                        except speech_recognition.RequestError as e:
                            print(f"Error making a request to the online recognition service; {e}")

            except speech_recognition.UnknownValueError:
                print("Sorry, I didn't catch that. Please try again.")
            except speech_recognition.RequestError as e:
                print(f"Error making a request to the online recognition service; {e}")

    if __name__ == "__main__":
        email_typing()
    
    @staticmethod
    def voice_typing():
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
                speak("started voice typing")
                while True:
                    
                    try:
                        audio = recognizer.listen(source, timeout=None)
                        text = recognizer.recognize_google(audio).lower()

                        if "stop typing" in text:
                            print("Exiting voice typing.")
                            speak("exiting voice typing")
                            break

                        if "full stop" in text:
                            text = text.replace("full stop", ". ")
                        else:
                            text += ""

                        if "space bar" in text:
                            text = text.replace("space bar", " ")

                        if "backspace" in text:
                            backspace()
                        else:
                            if "." not in text[-1]:
                                text += ""

                            print(f"Typed: {text}")
                            pyautogui.typewrite(text)

                    except speech_recognition.UnknownValueError:
                        print("Unknown value error. Continuing listening for commands.")
                        continue

    if __name__ == "__main__":
        voice_typing()

 
    @staticmethod
    def click_password(recognizer, src):
        while True:
            speech_to_txt = ""
            password_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_password.png", confidence=0.8 )
            pyautogui.moveTo(password_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked password button:" + speech_to_txt)

 
    @staticmethod
    def click_login(recognizer, src):
        while True:
            speech_to_txt = ""
            login_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_login.png", confidence=0.8 )
            pyautogui.moveTo(login_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked login button:" + speech_to_txt)

    @staticmethod
    def click_register(recognizer, src):
        while True:
            speech_to_txt = ""
            register_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_register.png", confidence=0.8 )
            pyautogui.moveTo(register_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked register button:" + speech_to_txt)

    @staticmethod
    def click_goback(recognizer, src):
        while True:
            speech_to_txt = ""
            goback_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_GoBack.png", confidence=0.8 )
            pyautogui.moveTo(goback_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked register button:" + speech_to_txt)

    @staticmethod
    def click_ok(recognizer, src):
        while True:
            speech_to_txt = ""
            ok_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_ok.png", confidence=0.8 )
            pyautogui.moveTo(ok_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked ok button:" + speech_to_txt)

    @staticmethod
    def click_gotoexam(recognizer, src):
        while True:
            speech_to_txt = ""
            go_to_exam_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_gotoexam.png", confidence=0.8 )
            pyautogui.moveTo(go_to_exam_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked gotoexam button:" + speech_to_txt)

    @staticmethod
    def click_startexam(recognizer, src):
        while True:
            speech_to_txt = ""
            start_exam_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_start_exam.png", confidence=0.8 )
            pyautogui.moveTo(start_exam_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked start exam button:" + speech_to_txt)

    @staticmethod
    def voice_scroll():
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            speak("Listening for the scroll command...")
            print("Listening for the scroll command...")

            while True:
                audio = recognizer.listen(source)

                try:
                    command = recognizer.recognize_google(audio)
                    if "stop scrolling" in command:
                        speak("Stopping scrolling.")
                        print("Stopping scrolling.")
                        break
                    elif "scroll up" in command:
                        print("Scrolling up.")
                        pyautogui.scroll(300)
                    elif "scroll down" in command:
                        print("Scrolling down.")
                        pyautogui.scroll(-300)
                    else:
                        speak("Sorry, I didn't catch that command. Please try again.")
                        print("Sorry, I didn't catch that command. Please try again.")
                except speech_recognition.UnknownValueError:
                    continue
                except speech_recognition.RequestError as e:
                    print(f"Error making a request to the online recognition service; {e}")

    if __name__ == "__main__":
        voice_scroll()
    
    @staticmethod
    def click_submitexam(recognizer, src):
        while True:
            speech_to_txt = ""
            submit_exam_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_submit_exam.png", confidence=0.8 )
            pyautogui.moveTo(submit_exam_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked submit exam button:" + speech_to_txt)

    @staticmethod
    def click_logout(recognizer, src):
        while True:
            speech_to_txt = ""
            logout_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_logout.png", confidence=0.8 )
            pyautogui.moveTo(logout_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked logout exam button:" + speech_to_txt)

    @staticmethod
    def click_myResult(recognizer, src):
        while True:
            speech_to_txt = ""
            myresult_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_MyResult.png", confidence=0.6 )
            pyautogui.moveTo(myresult_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked logout exam button:" + speech_to_txt)
    
    @staticmethod
    def click_subject(recognizer, src):
        while True:
            speech_to_txt = ""
            subject_button=pyautogui.locateCenterOnScreen("C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\command_images\\click_subject.png", confidence=0.6 )
            pyautogui.moveTo(subject_button)
            pyautogui.click()

            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio)
                
            except speech_recognition.UnknownValueError:
                pass
            print("clicked logout exam button:" + speech_to_txt)