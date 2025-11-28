import os 
os.system("cls")
from tkinter import *

def Mostrar():
    comentario=txt.get(1.0,END).strip()
    lbl_resultado.config(text=f"{comentario}")
    pass

ventana=Tk()
ventana.title("Uso de text")
ventana.geometry("600x400")

lbl1=Label(ventana,text="Escriba su comentario").pack()
txt=Text(ventana)
txt.config(width=40,
           height=5,
           border=5 )
txt.pack()

btn=Button(ventana,text="Mostrar comentario",command=Mostrar)
btn.pack()

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()




ventana.mainloop()
