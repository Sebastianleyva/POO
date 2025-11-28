import os 
os.system("cls")
from tkinter import *

def confirmar():
    lbl.config(text=f"Opcion seleccionada: {opcion.get()}")

ventana=Tk()
ventana.title("CheckBox en tkinter")
ventana.geometry("500x500")

opcion=StringVar()
rbtn=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="opcion1")
rbtn.pack()
rbtn1=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="opcion2")
rbtn1.pack()
rbtn2=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="opcion3")
rbtn2.pack()

btn1=Button(ventana,text="Mostrar selección",command=confirmar)
btn1.pack()

lbl=Label(ventana,text="")
lbl.pack()


ventana.mainloop()