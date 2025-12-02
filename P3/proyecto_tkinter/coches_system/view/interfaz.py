from tkinter import *
from tkinter import messagebox


class Interfaz():
    def __init__(ventana):
        ventana.title("Coches_system")
        ventana.geometry("800x500")
        ventana.resizable(False,False)
        Interfaz.menu_principal(ventana)
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    @staticmethod
    def menu_principal(ventana):
        Interfaz.borrarPantalla(ventana)
        btn_autos=Button(ventana,text="Autos",command=lambda: Interfaz.menu_acciones(ventana))
        btn_autos.pack(pady=10)
        btn_camionetas=Button(ventana,text="Camionetas")
        btn_camionetas.pack(pady=10)
        btn_camiones=Button(ventana,text="Camiones")
        btn_camiones.pack(pady=10)
        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack(pady=10)
    @staticmethod
    def menu_acciones(ventana,tipo):
        Interfaz.borrarPantalla(ventana)
        lbl_tit=Label(ventana,text="..:: Menú de {tipo} ::..",font=("Arial",16))
        lbl_tit.pack(pady=10)
        btn_insertar=Button(ventana,text="Insertar")
        btn_insertar.pack(pady=10)
        btn_consultar=Button(ventana,text="Consutltar")
        btn_consultar.pack(pady=10)
        btn_actualizar=Button(ventana,text="Actualizar",command=lambda: Interfaz.buscar_autos(ventana))
        btn_actualizar.pack(pady=10)
        btn_Eliminar=Button(ventana,text="Eliminar")
        btn_Eliminar.pack(pady=10)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def autos_insertar(ventana):
        Interfaz.borrarPantalla(ventana)
        lbl_marca=Label(ventana,text="Marca")
        lbl_marca.pack(pady=10)
        etr_marca=Entry(ventana)
        etr_marca.pack(pady=5)
        lbl_color=Label(ventana,text="Color")
        lbl_color.pack(pady=10)
        etr_color=Entry(ventana)
        etr_color.pack(pady=5)
        lbl_modelo=Label(ventana,text="Mdelo")
        lbl_modelo.pack(pady=10)
        etr_modelo=Entry(ventana)
        etr_modelo.pack(pady=5)
        lbl_velocidad=Label(ventana,text="Velocidad")
        lbl_velocidad.pack(pady=10)
        etr_velocidad=Entry(ventana)
        etr_velocidad.pack(pady=5)
        btn_ingres=Button(ventana,text="Insertar")
        btn_ingres.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_autos(ventana))
        btn_regresar.pack()
    @staticmethod
    def autos_consular(ventana):
        pass
    @staticmethod
    def buscar_autos(ventana):
        Interfaz.borrarPantalla(ventana)
        lbl_id=Label(ventana,text="Ingresa el ID del carro a buscar")
        lbl_id.pack(pady=5)
        txt_id=Entry(ventana)
        txt_id.pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar")
        btn_buscar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_autos(ventana))
        btn_regresar.pack()
        pass
    @staticmethod
    def cambiar_autos(ventana):
        lbl_titulo=Label(ventana,text="..::Ingresa los siguientes datos del tipo {tipo} ::..")
        lbl_titulo.pack(pady=5)
        lbl_entrada=Label(ventana,text="Marca")
        lbl_entrada.pack(5)
        txt_entrada=Entry(ventana)
        txt_entrada.pack(pady=5)
        lbl_color=Label(ventana,text="Color")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)
        lbl_velocidad=Label(ventana,text="Velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velociad=Entry(ventana)
        txt_velociad.pack(pady=5)
        lbl_caballaje=Label(ventana,text="Caballaje")
        lbl_caballaje.pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)
        lbl_plazas=Label(ventana,text="Plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

    @staticmethod
    def borrar_autos(ventana):
        pass

