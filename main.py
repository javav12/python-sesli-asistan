from customtkinter import *
import sesli_asistan 
import threading

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")

#* asistanı baslatma
# sesliasistan = threading.Thread(target=sesli_asistan.mainf)
# sesliasistan.start()

#* arayüz tasarım
main = CTkFrame(master=app,fg_color="#1E1E1E",border_color="#1B1B1B",border_width=5,width=300, height=300)
main.pack(expand=True,)
label = CTkLabel(master=main,text="test deneme 1  2 3",width=300, height=00)
label.place(x=10,y=100)

#* test
for i in range(1000):
    label.configure(text=i*i*9*i*i)





#* arayüz baslatma
app.mainloop()