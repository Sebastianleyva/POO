import os 
os.system("cls")
from tkinter import *

def confirmar():
    if opcion.get()==1:
        lbl.config(text="Notificaciónes...Activadas")
    else:
        lbl.config(text="Notificaciónes...Desativadas")


ventana=Tk()
ventana.title("CheckBox en tkinter")
ventana.geometry("500x500")

opcion=IntVar()
chk=Checkbutton(ventana,text="¿Desea recibir notificaciones?",variable=opcion,onvalue=1,offvalue=0)
chk.pack()

btn1=Button(ventana,text="Confirmar",command=confirmar)
btn1.pack()

lbl=Label(ventana,text="")
lbl.pack()


ventana.mainloop()