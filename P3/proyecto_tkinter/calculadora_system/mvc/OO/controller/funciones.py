from view import interfaz
from tkinter import messagebox
from model import operaciones 

class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        messagebox.showinfo(icon="info",title=titulo,message=f"{numero1} {signo} {numero2}={resultado}")
        pregunta=messagebox.askquestion(message=f"¿Quires guardar la operación {numero1} {signo} {numero2}={resultado} en la base de datos?",icon="question")
        if pregunta=="yes":
            operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
            pass
