import os 
os.system("cls")
from tkinter import *

ventana=Tk()
ventana.title("Imagenes pillow en tkinter")
ventana.geometry("500x500")

def mensaje(tipo):
    rlbl.config(text=f"{tipo}")

#primer forma de agregar imagenes con la libreria de tkinter
#Photo img solo permite archivos .png, .gif y .pgm/.ppm
imagen=PhotoImage(file="logo.png")
# img=PhotoImage(file="Users\sebas\OneDrive\Documentos\POO\P3\introduccion_tkinter\logo.png")

# Obtener la ruta absoluta del directorio donde está este archivo .py
# ruta_base = os.path.dirname(os.path.abspath(_file_))

# # Construir la ruta completa al archivo de imagen
# ruta_imagen = os.path.join(ruta_base,"logo.png")

lbl=Label(ventana,image=imagen)
lbl.pack()

btn=Button(ventana,image=imagen, command=lambda: mensaje("Hola python"))

rlbl=Label(ventana,text="")
rlbl.pack()

ventana.mainloop()