"""Crear una calculadora
1.-Dos campos de texto
2.-cuatro botones para las operaciones
3.-Mostrar el resultado en una alerta
4.-Programación estructurada
5.-Implementar el MVC
"""
from view import interfaz
from tkinter import *

class App:
    def __init__(self, ventana):
        # crear una instancia de la clase Vistas para inicializar la UI
        self.view = interfaz.Vistas(ventana)
        
# def main():
#     interfaz.vista()

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
