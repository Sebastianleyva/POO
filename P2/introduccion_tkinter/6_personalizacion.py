import os
os.system("cls")
from tkinter import *

def cambiarLabel():
    etiqueta.config(
        text="POO con Python",
        background="darkblue",
        fg="white",
        cursor="circle")

def restaurarLabel():
    etiqueta.config(
        text="Bienvenidos a Tkinter",
        background="lightblue",
        fg="darkblue",
        font=("Helvetica",30,"italic"),
        width=50,
        height=4
    )

ventana= Tk()
ventana.title("Personalizar widgets y objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    background="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic")
)
etiqueta.pack(pady=25)

boton1=Button(ventana,text="Hax click aqui :)",command=cambiarLabel)
boton1=Button(ventana,text="Hax click aqui :)",command=cambiarLabel)
boton1.config(
    background="black",
    fg="white",
    font=("Times new roman",20,"bold"),
    width=15,
    activeforeground="Yellow",
)
boton1.pack(pady=5)

boton2=Button(ventana,text="Regresar valores",command="restaurarLabel")
boton2=Button(ventana,text="Regresar valores",command=restaurarLabel)
boton2.config(
    background="green",
    fg="black",
    font=("Times new roman",20,"bold"),
    width=15,
    activeforeground="red"
)
boton2.pack(pady=5)


ventana.mainloop()
