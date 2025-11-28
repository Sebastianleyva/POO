import os 
os.system("cls")
from tkinter import *

ventana=Tk()
ventana.title("Menus en tkinter")
ventana.geometry("500x500")

def mostrarestado(var1):
    lbl.config(text=f"{var1}")

menubar=Menu(ventana)
ventana.config(menu=menubar)

archivomenu=Menu(menubar, tearoff=False)
menubar.add_cascade(label="Archivo",menu=archivomenu)


archivomenu.add_command(label="Nuevo Archivo",command=lambda:mostrarestado("Nuevo Archivo"))
archivomenu.add_command(label="Guardar",command=lambda:mostrarestado("Guardar"))
archivomenu.add_separator()
archivomenu.add_command(label="Salir",command=ventana.destroy)

editarmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="Edicion",menu=editarmenu)

editarmenu.add_command(label="Copiar",command=lambda:mostrarestado("Copiar"))
editarmenu.add_command(label="Recortar",command=lambda:mostrarestado("Recortar"))
editarmenu.add_separator()
editarmenu.add_command(label="Salir",command=ventana.destroy)

# btn1=Button(ventana,text="Mostrar selección del ususario",command="confirmar")
# btn1.pack()

lbl=Label(ventana,text="")
lbl.pack()

ventana.mainloop()