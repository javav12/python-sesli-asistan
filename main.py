#
#* kütüphaneler
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
import datetime
import webbrowser

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("anlayamadım")
        except sr.RequestError:
            print("sistem hatası")
        return voice


def speak(string):
    tts= gTTS(text=string,lang="tr",slow=False)
    file= "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
playsound("startup.mp3")
def wp(voice):
    if "hey" in voice or "asistan" in voice:
            playsound("ac.mp3")
            speak("efendim")
            voice=record()
            if voice != "":
                voice = voice.lower()
                rp(voice)
                print(voice)
            voice = ""
def rp(voice):
    if "merhaba" in voice:
            speak("merhaba")
    if "sistemi kapat" in voice:
            speak("sistem kapatılıyor")
            time.sleep(1)
            speak("3")
            time.sleep(1)
            speak("2")
            time.sleep(1)
            speak("1")
            time.sleep(1)
            speak("0")
            playsound("shutdown.mp3")
            exit()
    if "saat kaç" in voice:
            speak(datetime.datetime.now().strftime("%H:%M"))
    if "google'da ara" in voice:
        speak("ne aratayim?")
        search = record()
        url="https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için google'da bulabildiklerimi listeliyorum".format(search))
    if "not et" in voice:
        speak("dosya ismi ne olsun")
        fn = record() + ".txt"
        speak("ne kaydetmek istiyorsun")
        tt = record()
        f= open(fn, "w",encoding="utf-8")
        f.writelines(tt)
        f.close()



while True:
    voice=record()
    if voice != "":
        voice = voice.lower()
        wp(voice)
        print(voice)
        voice = ""

