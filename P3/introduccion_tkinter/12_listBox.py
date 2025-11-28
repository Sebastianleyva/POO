import os 
os.system("cls")
from tkinter import *

ventana=Tk()
ventana.title("listBox en tkinter")
ventana.geometry("500x500")

def confirmar():
    seleccion=lbx.get(lbx.curselection())
    lbl.config(text=f"Usted selecciono el colo: {seleccion}")
    pass

lbx=Listbox(ventana,height=5,width=20,selectmode="single")
lbx.pack()
opciones=["amarillo","rojo","azul","verde"]
for i in opciones:
    lbx.insert(END,i)

btn1=Button(ventana,text="Mostrar selección del ususario",command=confirmar)
btn1.pack()

lbl=Label(ventana,text="")
lbl.pack()

ventana.mainloop()