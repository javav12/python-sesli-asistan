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
# import qrcodeg 
def kapat():
         exit()
#* ana fonlsiyon
def mainf():
    #* değiskenler
    config = ConfigParser()
    r = sr.Recognizer()
    ini_var = False
    linux = False
    #* settings.ini dosyasını kontrol etmek
    dl = os.listdir()
    for i in dl:
        if i == "settings.ini":
            ini_var= True

    #* settings.ini dosyası varsa yapay zeka ayarlamak
    if ini_var == True:
        config.read('settings.ini')
        api = config['API_KEY']['google_genetive_ai_api']
        genai.configure(api_key=api)
        model_gemini_pro = genai.GenerativeModel('gemini-pro')

    

    #* sesi kaydetmek
    def record(ask=False):
        with sr.Microphone() as source:
            if ask:
                pass
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("sistem hatası")
            return voice

    #* konusma
    def speak(string):
        tts= gTTS(text=string,lang="tr",slow=False)
        file= "answer.mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)

    #* açılıs sesini oynatma
    playsound("startup.mp3")
    if ini_var == False:
        speak("Uyarı! settings.ini dosyası bulunamadı veya adı yanlış assistan çalışmaya devam eder ama yapay zeka çalışamaz")

    #* asistan aktiflestirme
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

    #* yanıtlar
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
        if "yapay zeka" in voice and ini_var == True:
            speak("yapay zekada ne aratmak istersiniz")
            promt = record()
            rp = model_gemini_pro.generate_content(promt)
            speak(str(rp.text))
            
        if "yapay zeka" in voice and ini_var == False:
            speak("settings.ini dosyası bulunamadı veya adı yanlış")
        if "qr code" in voice or "qr kode" in voice or "qr kodu"in voice or "qr codu" in voice :
            speak("QR Code'un içine girceğiniz metin veya url ")
            # qrcodeg.baslat()
            speak("qr codunuz qrcodes klasörüne kaydedildi")
    #*ses dinleme
    while True:
        voice=record()
        if voice != "":
            voice = voice.lower()
            if voice == "sistemi kapat":
                rp(voice)
            wp(voice)
            print(voice)
            voice = ""


