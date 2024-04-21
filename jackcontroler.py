import subprocess
import time
import os
#* değiskenler
linux = False
#* komutlar
komut = ["jack_control","start"] 
komut2 = ["jack_control","exit"]
#* terminale komutların yazımı
def terminal_komutu_calistir(komut):
    islem = subprocess.Popen(komut, stdout=subprocess.PIPE)
    cikti, hata = islem.communicate()
    cikti_metni = cikti.decode()
    return cikti_metni
#* isletim sistemi kontrolü
def kontrol():
    for i in os.uname():
        if "Linux" in i or i == "Fedora":
            print(i)
            linux = True
            return linux
#* jack serverinin baslatılması
def jack_baslat():
    cikti_metni = terminal_komutu_calistir(komut)
    print(cikti_metni)
#* jack serverinin durdurulması
def jack_durdur():
    cikti_metni = terminal_komutu_calistir(komut2)
    print(cikti_metni)