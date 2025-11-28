from tkinter import *
from tkinter import messagebox
import os
os.system("cls")
from controller import funciones
import main
from model import operaciones

class Vistas():
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("800x500")
        ventana.resizable(False,False)
        self.vista(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()


    def menu_principal(self,ventana):
        menubar=Menu(ventana)
        ventana.config(menu=menubar)

        operacionmenu=Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Operaciones",menu=operacionmenu)

        operacionmenu.add_command(label="Agregar",command=lambda: self.vista(ventana))
        operacionmenu.add_command(label="Consultar",command=lambda: "")
        operacionmenu.add_command(label="Guardar",command=lambda: "")
        operacionmenu.add_command(label="Borrar",command= lambda: self.Borrar(ventana)) 
        operacionmenu.add_separator()
        operacionmenu.add_command(label="Salir",command=ventana.quit())

    def vista(self,ventana):
        self.borrarPantalla(ventana)
        self.menu_principal(ventana)

        num1=IntVar()
        num2=IntVar()
        txt1=Entry(ventana,textvariable=num1,width=5,justify=RIGHT)
        txt1.focus()
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

        btn1=Button(marco,text="+",command=lambda: funciones.Controladores.operaciones("Sumar",num1.get(),num2.get(),"+"))
        btn1.grid(row=0,column=0,padx=5,pady=5)
        btn2=Button(marco,text="-",command=lambda: funciones.Controladores.operaciones("Restar",num1.get(),num2.get(),"-"))
        btn2.grid(row=0,column=1,padx=5,pady=5)
        btn3=Button(marco,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicar",num1.get(),num2.get(),"x"))
        btn3.grid(row=0,column=2,padx=5,pady=5)
        btn4=Button(marco,text="÷",command=lambda: funciones.Controladores.operaciones("Dividir",num1.get(),num2.get(),"/"))
        btn4.grid(row=0,column=3,padx=5,pady=5)

        btn5=Button(ventana,text="salir",command=ventana.quit)
        btn5.pack()
    

    def Borrar(self,ventana):
        self.menu_principal(ventana)
        self.borrarPantalla(ventana)
        self.menu_principal(ventana)
        lbl=Label(ventana,text="Borrar una operación").pack()
        lbl2=Label(ventana,text="Ingrese el ID de la operación a borrar").pack()
        id_op=IntVar()
        txt_id=Entry(ventana,textvariable=id_op,width=5,justify=RIGHT)
        txt_id.focus()
        txt_id.pack()
        btn_borrar=Button(ventana,text="Borrar",command=lambda: operaciones.Operaciones.eliminar(id_op.get()))
        btn_borrar.pack()
        btn_salir=Button(ventana,text="Volver",command= lambda: self.vista(ventana))
        btn_salir.pack()

