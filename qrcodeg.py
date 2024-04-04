import qrcode
import os
ky = False






qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
def kontrol():
    ky = False
    if  "qrcodes" not in os.listdir():
        ky = True
    if ky == True:
        os.mkdir("qrcodes")

def mkqr(data):
    kontrol()
    qrs = len(os.listdir("qrcodes"))
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcodes/QR({}).png".format(qrs))

import tkinter as tk

form = tk.Tk()
form.geometry('300x50')
form.state('normal')

form.title("QR CODE İçerik ")
yazi = tk.Label(form,text="ok tusuna bastıktan sonra pencereyi kapatın")
yazi.pack()
giris = tk.Entry(fg="black",bg="white")
giris.pack()


def veri_cek():
    veri=giris.get()
    mkqr(veri)

button = tk.Button(text="OK",fg="black",bg="white",command=veri_cek)
button.pack()

etiket=tk.Label()
etiket.pack()

def baslat():
    form.mainloop()
