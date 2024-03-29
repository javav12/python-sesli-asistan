import tkinter as tk

form = tk.Tk()
form.geometry('300x50+50+50')
form.title("QR CODE İçerik ")
giris = tk.Entry(fg="black",bg="white")
giris.pack()

def veri_cek():
    veri=giris.get()
    print(veri)
button = tk.Button(text="OK",fg="black",bg="white",command=veri_cek)
button.pack()

etiket=tk.Label()
etiket.pack()

def baslat():
    form.mainloop()

#! TEST
baslat()
