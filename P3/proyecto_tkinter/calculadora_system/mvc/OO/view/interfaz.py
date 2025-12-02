from tkinter import *
from tkinter import messagebox
import os
os.system("cls")
from controller import funciones
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
        operacionmenu.add_command(label="Consultar",command=lambda: self.consultar(ventana))
        operacionmenu.add_command(label="Guardar",command=lambda: "")
        operacionmenu.add_command(label="Borrar",command= lambda: self.buscar(ventana))
        operacionmenu.add_separator()
        # pasar la referencia a la función sin ejecutarla
        operacionmenu.add_command(label="Salir",command=ventana.quit)

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
    
    def Borrar(self,ventana, id_prefill=None):
        self.menu_principal(ventana)
        self.borrarPantalla(ventana)
        self.menu_principal(ventana)
        lbl=Label(ventana,text="Borrar una operación").pack()
        lbl2=Label(ventana,text="Ingrese el ID de la operación a borrar").pack()
        id_op=IntVar()
        # Si se pasó un id_prefill, asignarlo al IntVar para prellenar el Entry
        if id_prefill is not None:
            try:
                id_op.set(id_prefill)
            except Exception:
                pass
        txt_id=Entry(ventana,textvariable=id_op,width=5,justify=RIGHT)
        txt_id.focus()
        txt_id.pack()

        def on_borrar():
            id_val = id_op.get()
            confirmado = operaciones.Operaciones.eliminar(id_val)
            if confirmado:
                messagebox.showinfo(title="Operación eliminada", message=f"La operación con ID {id_val} fue eliminada")
                self.vista(ventana)
            else:
                messagebox.showerror(title="Error", message=f"No se pudo eliminar la operación con ID {id_val}")

        btn_borrar=Button(ventana,text="Borrar",command=on_borrar)
        btn_borrar.pack()
        btn_salir=Button(ventana,text="Volver",command= lambda: self.vista(ventana))
        btn_salir.pack()

    def buscar(self,ventana):
        self.menu_principal(ventana)
        self.borrarPantalla(ventana)
        self.menu_principal(ventana)
        lbl1=Label(ventana,text="Ingrese el ID de la operación a buscar")
        lbl1.pack(pady=10)
        id_var=IntVar()
        txt1=Entry(ventana,textvariable=id_var,width=5,justify=RIGHT)
        txt1.pack(pady=5)

        def on_buscar():
            try:
                id_val = id_var.get()
            except Exception:
                messagebox.showerror(title="ID inválido", message="Ingrese un ID numérico")
                return

            resultado = operaciones.Operaciones.buscar(id_val)
            if resultado is None:
                messagebox.showinfo(title="No encontrado", message="La operación no existe")
            else:
                messagebox.showinfo(title="Encontrado", message="Operación encontrada.")
                self.Borrar(ventana, id_val)

        btn1=Button(ventana,text="Buscar",command=on_buscar)
        btn1.pack(pady=5)
        
    def consultar(self, ventana):
        """Interfaz para consultar operaciones: buscar por ID y listar todas."""
        self.borrarPantalla(ventana)
        self.menu_principal(ventana)

        lbl=Label(ventana, text="Consultar operaciones")
        lbl.pack(pady=5)

        # Búsqueda por ID
        frame_buscar = Frame(ventana)
        frame_buscar.pack(pady=5)
        id_var = IntVar()
        txt_id = Entry(frame_buscar, textvariable=id_var, width=8, justify=RIGHT)
        txt_id.pack(side=LEFT)

        def on_consultar_id():
            try:
                id_val = id_var.get()
            except Exception:
                messagebox.showerror(title="ID inválido", message="Ingrese un ID numérico")
                return

            data = operaciones.Operaciones.consultar(id_val)
            if data is None:
                messagebox.showinfo(title="No encontrado", message="La operación no existe")
                return

            detalle = f"ID: {data['id']}\nFecha: {data['fecha']}\nOperación: {data['numero1']} {data['signo']} {data['numero2']} = {data['resultado']}"
            messagebox.showinfo(title="Encontrado", message=detalle)
            # Preguntar si desea eliminarla
            if messagebox.askyesno(title="Eliminar", message="¿Desea eliminar esta operación?"):
                self.Borrar(ventana, id_val)

        btn_consultar = Button(frame_buscar, text="Buscar", command=on_consultar_id)
        btn_consultar.pack(side=LEFT, padx=5)

        # Listado completo
        lbl2 = Label(ventana, text="Todas las operaciones:")
        lbl2.pack(pady=5)

        frame_list = Frame(ventana)
        frame_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar = Scrollbar(frame_list, orient=VERTICAL)
        listbox = Listbox(frame_list, yscrollcommand=scrollbar.set, width=100)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        operaciones_all = operaciones.Operaciones.mostrar()
        for row in operaciones_all:
            try:
                texto = f"ID:{row[0]} | {row[1]} | {row[2]} {row[4]} {row[3]} = {row[5]}"
            except Exception:
                texto = str(row)
            listbox.insert(END, texto)

        def on_double_click(evt):
            sel = listbox.curselection()
            if not sel:
                return
            idx = sel[0]
            line = listbox.get(idx)
            try:
                id_val = int(line.split("|")[0].replace("ID:","").strip())
            except Exception:
                return
            data = operaciones.Operaciones.consultar(id_val)
            if data:
                detalle = f"ID: {data['id']}\nFecha: {data['fecha']}\nOperación: {data['numero1']} {data['signo']} {data['numero2']} = {data['resultado']}"
                messagebox.showinfo(title="Detalle", message=detalle)
                if messagebox.askyesno(title="Eliminar", message="¿Desea eliminar esta operación?"):
                    self.Borrar(ventana, id_val)

        listbox.bind('<Double-1>', on_double_click)