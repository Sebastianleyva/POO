from tkinter import *
from tkinter import messagebox
import os
os.system("cls")
from controller import funciones

def vista():
    ventana=Tk()
    ventana.title("Calculadora")
    ventana.geometry("350x500")
    ventana.resizable(False,False)

    num1=IntVar()
    num2=IntVar()
    txt1=Entry(ventana,textvariable=num1,width=5,justify=RIGHT)
    txt1.pack()
    txt2=Entry(ventana,textvariable=num2,width=5,justify=RIGHT)
    txt2.pack()

    marco=Frame(ventana)
    marco.config(
        width=800,
        height=300,
        bg="silver"
    )
    marco.pack_propagate(False)
    marco.pack()

    btn1=Button(marco,text="+",command=lambda: funciones.operaciones("Sumar",num1.get(),num2.get(),"+"))
    btn1.grid(row=0,column=0,padx=5,pady=5)
    btn2=Button(marco,text="-",command=lambda: funciones.operaciones("Restar",num1.get(),num2.get(),"-"))
    btn2.grid(row=0,column=1,padx=5,pady=5)
    btn3=Button(marco,text="x",command=lambda: funciones.operaciones("Multiplicar",num1.get(),num2.get(),"x"))
    btn3.grid(row=0,column=2,padx=5,pady=5)
    btn4=Button(marco,text="÷",command=lambda: funciones.operaciones("Dividir",num1.get(),num2.get(),"÷"))
    btn4.grid(row=0,column=3,padx=5,pady=5)


    btn5=Button(ventana,text="salir",command=ventana.quit)
    btn5.pack()

    ventana.mainloop()