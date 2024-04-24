
              ░██████╗███████╗░██████╗██╗░░░░░██╗
              ██╔════╝██╔════╝██╔════╝██║░░░░░██║
              ╚█████╗░█████╗░░╚█████╗░██║░░░░░██║
              ░╚═══██╗██╔══╝░░░╚═══██╗██║░░░░░██║
              ██████╔╝███████╗██████╔╝███████╗██║


    ░█████╗░░██████╗██╗░██████╗████████╗░█████╗░███╗░░██╗
    ██╔══██╗██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║
    ███████║╚█████╗░██║╚█████╗░░░░██║░░░███████║██╔██╗██║
    ██╔══██║░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║
    ██║░░██║██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝

                                      ░░█ ▄▀█ █░█ ▄▀█ █░█ ▄█ ▀█
                                      █▄█ █▀█ ▀▄▀ █▀█ ▀▄▀ ░█ █▄





Proje fikrim: sesli asistan yapıp veri cekeren ve bunu grafiklestirip kulanıcıya sunan asistan(cok fazla özeliği olacak)


Proje temellerini aldığım kaynak: https://www.youtube.com/watch?v=n6tzXfnp6A8&list=PLRb-ja_tK-M0S9qnX0mAXn2ghBul8abmQ

Kütüphaneler requirements.txt de





█▄▀ █░█ █▀█ █░█ █░░ █░█ █▀▄▀█ ▀
█░█ █▄█ █▀▄ █▄█ █▄▄ █▄█ █░▀░█ ▄

    windows:
        pip -r requirements.txt
    linux:
        pip3 -r requirements.txt
        (eğer pyaudio ile ilgili hata alıyorsanız internete aratmanız lazım ama bu siteyi inceleye  bilir sinizhttps://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)



█▀▀ ▄▀█ █░░ █ █▀ ▀█▀ █ █▀█ █▀▄▀█ ▄▀█ ▀
█▄▄ █▀█ █▄▄ █ ▄█ ░█░ █ █▀▄ █░▀░█ █▀█ ▄

    windows:
        tüm paketleri kurduktan sonra main.py ı çalıstırın
    linux:
        tüm paketleri kurduktan sonra sırası ile:
            jack_control start
            python3 main.py veya ide den baslatın
            programı kapatırken:
                jack_control exit
                yazınız





█▄█ ▄▀█ █▀█ ▄▀█ █▄█   ▀█ █▀▀ █▄▀ ▄▀█ ▀
░█░ █▀█ █▀▀ █▀█ ░█░   █▄ ██▄ █░█ █▀█ ▄

     https://makersuite.google.com/app/apikey adresine gidip bir api key alın 
     settings.ini dosyasını olusturun ardından içine 

        "[API_KEY]
        google_genetive_ai_api = api keyiniz"

    yazınız ve api keyinizi giriniz
    artık yapay zeka çalısır
    Eyer yardıma ihtiyacınız varsa:https://ai.google.dev/tutorials/python_quickstart rehberine baka bilirsiniz


