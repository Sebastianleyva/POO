import os 
os.system("cls")
from tkinter import *

ventana=Tk()
ventana.title("Distribucion")
ventana.geometry("600x400")

#Opcion 1 pack-side

# lbl1=Label(ventana,text="Escriba su usuario").pack(anchor="nw",side=TOP,padx=5,pady=5)
# # txt1=Entry(ventana).pack(side=LEFT)

# lbl2=Label(ventana,text="Escriba su contraseña").pack(anchor="nw",side=TOP,padx=5,pady=5)
# # txt2=Entry(ventana,sho="*").wpack()

#Opcion 2 con el grid
lbl1=Label(ventana,text="Escriba su usuario").grid(row=0,column=0,padx=5,pady=5)
Entry(ventana).grid(row=0,column=1,padx=5,pady=5)
lbl2=Label(ventana,text="Escriba su contraseña").grid(row=1,column=0,padx=5,pady=5)
Entry(ventana).grid(row=1,column=1,padx=5,pady=5)



ventana.mainloop()
