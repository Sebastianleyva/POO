"""Crear una calculadora
1.-Dos campos de texto
2.-cuatro botones para las operaciones
3.-Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox
import os
os.system("cls")


def sumar():
    suma=num1.get()+num2.get()
    alerta(suma,"+")
    pass
def restar():
    resta=num1.get()-num2.get()
    alerta(resta,"-")
def multiplicar():
    mult=num1.get()*num2.get()
    alerta(mult,"*")
def dividir():
    divi=num1.get()/num2.get()
    alerta(divi,"÷")

# def operaciones():
#     operacion=input(f"""¿Qué operación desea realizar?
#                     1.-suma
#                     2.-resta
#                     3.-multiplicación
#                     4.-dvisión""").strip()
#     match operacion:
#         case "1":
#             suma=num1.get()+num2.get()
#             # alerta(suma,"+")
#         case "2":
#             resta=num1.get()-num2.get()
#             # alerta(resta,"-")
#         case "3":
#             mult=num1.get()*num2.get()
#             # alerta(mult,"*")4
#         case "4":
#             divi=num1.get()/num2.get()
#             # alerta(divi,"÷")
#         case _:
#             print("no valido")
#     messagebox.showinfo(message=f"el resultado de {num1.get()} {operacion} {num2.get()} es:  {divi}",icon="info")


def alerta(resultado,operacion):
   resultado=messagebox.showinfo(message=f"el resultado de {num1.get()} {operacion} {num2.get()} es:  {resultado}",icon="info")

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

btn1=Button(marco,text="+",command=sumar)
btn1.grid(row=0,column=0,padx=5,pady=5)
btn2=Button(marco,text="-",command=restar)
btn2.grid(row=0,column=1,padx=5,pady=5)
btn3=Button(marco,text="x",command=multiplicar)
btn3.grid(row=0,column=2,padx=5,pady=5)
btn4=Button(marco,text="÷",command=dividir)
btn4.grid(row=0,column=3,padx=5,pady=5)


btn5=Button(ventana,text="salir",command=ventana.quit)
btn5.pack()

ventana.mainloop()