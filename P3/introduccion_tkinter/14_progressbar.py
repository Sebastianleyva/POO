import os 
os.system("cls")
from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Progressbar en tkinter")
ventana.geometry("500x500")

def progreso():
    barrap["value"]=0
    barrap.update()
    for i in range(101):
        barrap["value"]=i
        ventana.update()
        ventana.after(50)

barrap=ttk.Progressbar(ventana,mode="determinate", orient="horizontal",length=200,)
barrap.pack()

btn=Button(ventana,text="Iniciar progreso",command=progreso)
btn.pack()

ventana.mainloop()