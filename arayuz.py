import tkinter as tk
import qrcodeg

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
    qrcodeg.mkqr(veri)

button = tk.Button(text="OK",fg="black",bg="white",command=veri_cek)
button.pack()

etiket=tk.Label()
etiket.pack()

def baslat():
    form.mainloop()

