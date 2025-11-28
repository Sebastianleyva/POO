import os 
os.system("cls")
from tkinter import *

def confirmar():
    lbl.config(text=f"Valor seleccionado por el usuario...{valor.get()}")


ventana=Tk()
ventana.title("CheckBox en tkinter")
ventana.geometry("500x500")


valor=IntVar()
scl=Scale(ventana,from_=0,to=100,orient="horizontal",variable="valor")
scl.pack()

btn1=Button(ventana,text="Mostrar valor",command=confirmar)
btn1.pack()

lbl=Label(ventana,text="")
lbl.pack()


ventana.mainloop()