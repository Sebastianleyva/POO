import os
os.system("cls")
from tkinter import *

def saludarBoton():
    # nombre=entrada.get()
    lbl_1.config(
        text=f"Bienvenido {usuario.get()}"
    )

def aceptar():
    lbl_4.config(
        text=f"Bienvenido {usuario.get()}"
    )
    

def borrar_tx():
    txt_1.delete(0,END)
    txt_2.delete(0,END)
    lbl_4.config(text="")

def Salir():
    # ventana.quit()
    ventana.destroy()
    pass

ventana=Tk()
ventana.title("Entry")
ventana.geometry("800x800")

# etiqueta=Label(ventana,text="Ingrese su nombre")
# etiqueta.pack(padx=5)

# nombre=StringVar()
# entrada=Entry(ventana,textvariable=nombre)
# entrada.pack()
# # entrada.pack(pady=5)

# boton1=Button(ventana,text="Saludar",command=saludarBoton)
# boton1.pack()

# lbl=Label(ventana,text="")
# lbl.pack()

lbl_1=Label(ventana,text="Acceso al sistema")
lbl_1.config(
    background="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic")
)
lbl_1.pack(pady=5)

marco=Frame(ventana)
marco.config(
    width=800,
    height=300,
    bg="silver"
)
marco.pack_propagate(False)
marco.pack()

lbl_2=Label(marco,text="Nombre de ususario")
lbl_2.config(bg="silver")
lbl_2.grid(row=0,column=0,padx=5,pady=5)
usuario=StringVar()
txt_1=Entry(marco,textvariable=usuario)
txt_1.grid(row=0,column=1,padx=5,pady=5)

lbl_3=Label(marco,text="Contraseña")
lbl_3.config(bg="silver")
lbl_3.grid(row=1,column=1,padx=5,pady=5)
txt_2=Entry(marco,show="*")
txt_2.grid(row=1,column=0,padx=5,pady=5)


marco2=Frame(ventana)
marco2.config(
    width=800,
    height=300,
    bg="silver"
)
marco2.pack_propagate(False)
marco2.pack()

btn_1=Button(marco2,text="Aceptar",command=aceptar)
btn_1.grid(row=0,column=0,padx=5,pady=5)

btn_2=Button(marco2,text="Borrar",command=borrar_tx)
btn_2.grid(row=0,column=1,padx=5,pady=5)

btn_3=Button(marco2,text="Salir",command=Salir)
btn_3.grid(row=0,column=2,padx=5,pady=5)

lbl_4=Label(ventana,text="")
lbl_4.pack()




ventana.mainloop()