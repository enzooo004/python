from tkinter import *
from tkinter.ttk import *
from reproductor import *
musica = Reproductor   ('wefere (1).mp3')
def play_musica ():
    musica.volumen(0.8)
    musica.play()
def pause():
    musica.pause()
master = Tk()
master.geometry("200x200")

Label= Label(master, text= "Reproductor de musica")
Label.pack(pady=10)
btn_play = Button(master,text="▶️", command= play_musica)
btn_play.pack(pady=10)
btn_play = Button(master,text="⏸️", command= pause)
btn_play.pack(pady=10)

mainloop()