import speech_recognition as sr
import random
import pyautogui as p
import pyttsx3
print("A VERY BASIC SPEECH RECOGNITION GAME BASED ON ADDITION ")
engine = pyttsx3.init("sapi5")# TSS Engine, sapi5 - SAPI5 on Windows, #nsss - NSSpeechSynthesizer on Mac OS X, #espeak - eSpeak on every other platform
r = sr.Recognizer()# object for voice recognization
s=" "
count = 0
while(s!="exit"):
    print("Running")
    engine.say("Say Something") 
    engine.say("Next Word")
        engine.runAndWait()
    with sr.Microphone() as source:
        try:
            print(count)
            count+=1
            r.adjust_for_ambient_noise(source)
            print("Say your command...")
            audio = r.listen(source,timeout=10)
            print("Recognizing your voice...")
            text = r.recognize_google(audio)# USES GOOGLE API
            s=text
            print(text)
            text=text.lower()
            if(text=="t" or text=="T"):
                p.hotkey('ctrl', 't')
            elif(text=="play"):
                p.press("space")
            elif(text=="stop"):
                p.press("space")
            elif(text=="next"):
                p.press("right")
            elif(text=="back" ):
                p.press("left")
            elif(text=="full"):
                p.press("f")
            elif(text=="mini"):
                p.press("i")
            elif(text=="mute"):
                p.press("m")
            elif(text=="unmute"):
                p.press("m")
            elif(text=="subtitles"):
                p.press("c")
            elif(text=="cinema"):
                p.press("t")
            elif(text=="exit" or text=="end"):
                break
            else:
                print("Say again...")
            print("**********")
            print("I heard this ", text)
        except:
            print("----------------------------------- ")
