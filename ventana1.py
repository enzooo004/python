from tkinter import *
from tkinter import ttk
from controladores import abrirCalculadora 
from controladores import abrirPaint
from controladores import mostrarHora
ventana = Tk ()   
ventana.title("Primera ventana")
ventana.geometry("520x420")
ventana.iconbitmap("logo1.ico")
ventana.config(background="black")
botonCalculadora = Button(text="Calculadora", command=abrirCalculadora)
botonCalculadora.place(x=50,y=50)
botonPait = Button(text="Paint", command=abrirPaint)
botonPait.place(x=150,y=50)
botonhora = Button(text="Ver hora", command=mostrarHora)
botonhora.place(x=220,y=50)
ventana.mainloop()