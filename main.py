#
#* kütüphaneler
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
import datetime
import webbrowser
from configparser import ConfigParser
import google.generativeai as genai


#* değiskenler
config = ConfigParser()
config.read('settings.ini')
api = config['API_KEY']['google_genetive_ai_api']

#* ayarlamalar
genai.configure(api_key=api)
r = sr.Recognizer()

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
model_gemini_pro = genai.GenerativeModel('gemini-pro')


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
    if "sistem" in voice or "asistan" in voice or "hey asistan" in voice or "hey sistem" in voice or "system" in voice:
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
    if "orman yangınları nedir"in voice:
        speak("Orman yangınları, sadece Türkiye'yi değil, tüm dünyayı etkileyen bir sorundur. Her yıl milyonlarca hektar ormanlık alan yok olmaktadır. Bu durum, küresel ısınmaya ve iklim değişikliğine katkıda bulunmaktadır.Orman yangınları ile mücadele için uluslararası iş birliği şarttır. Ormanların korunması ve yangınların önlenmesi için ortak çalışmalar yapılmalıdır.")
    if "yapay zeka" in voice:
        speak("yapay zekada ne aratmak istersiniz")
        promt = record()
        rp = model_gemini_pro.generate_content(promt)
        speak(str(rp.text))
while True:
    voice=record()
    if voice != "":
        voice = voice.lower()
        wp(voice)
        print(voice)
        voice = ""

