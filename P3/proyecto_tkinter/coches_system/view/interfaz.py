from tkinter import *
from tkinter import messagebox
from controller import controlador


class Interfaz():
    def __init__(self,ventana):
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
        btn_autos=Button(ventana,text="Autos",command=lambda: Interfaz.menu_acciones(ventana,"Autos"))
        btn_autos.pack(pady=10)
        btn_camionetas=Button(ventana,text="Camionetas",command=lambda: Interfaz.menu_acciones(ventana,"Camionetas"))
        btn_camionetas.pack(pady=10)
        btn_camiones=Button(ventana,text="Camiones",command=lambda: Interfaz.menu_acciones(ventana,"Camiones"))
        btn_camiones.pack(pady=10)
        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack(pady=10)
    @staticmethod
    def menu_acciones(ventana,tipo):
        Interfaz.borrarPantalla(ventana)
        lbl_tit=Label(ventana,text=f"..:: Menú de {tipo} ::..",font=("Arial",16))
        lbl_tit.pack(pady=10)
        btn_insertar=Button(ventana,text="Insertar",command=lambda: Interfaz.autos_insertar(ventana))
        btn_insertar.pack(pady=10)
        btn_consultar=Button(ventana,text="Consutltar")
        btn_consultar.pack(pady=10)
        btn_actualizar=Button(ventana,text="Actualizar",command=lambda: Interfaz.cambiar_autos(ventana))
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
        lbl_caballaje=Label(ventana,text="Caballaje")
        lbl_caballaje.pack(pady=10)
        etr_caballaje=Entry(ventana)
        etr_caballaje.pack(pady=5)
        lbl_plazas=Label(ventana,text="Plazas")
        lbl_plazas.pack(pady=10)
        etr_plazas=Entry(ventana)
        etr_plazas.pack(pady=5)
        btn_ingres=Button(ventana,text="Insertar" ,command=lambda:controlador.Controlador_autos.registrar_auto("Autos",
                    etr_color.get(),
                    etr_marca.get(),
                    etr_modelo.get(),
                    etr_velocidad.get(),
                    etr_caballaje.get(),
                    etr_plazas.get()))
        btn_ingres.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_autos(ventana))
        btn_regresar.pack()
    @staticmethod
    def buscar_autos(ventana):
        Interfaz.borrarPantalla(ventana)
        lbl_id=Label(ventana,text="Ingresa el ID del vehiculo")
        lbl_id.pack(pady=5)
        txt_id=Entry(ventana)
        txt_id.pack(pady=5)
        def on_buscar():
            id=txt_id.get()
            if id.isdigit():
                Interfaz.mostrar_autos(ventana)
            else:
                messagebox.showerror("Error","El ID debe ser un número entero")
        btn_buscar=Button(ventana,text="Buscar",command=lambda:on_buscar())
        btn_buscar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana,"auto"))
        btn_regresar.pack()
        pass
    @staticmethod
    def cambiar_autos(ventana):
        Interfaz.buscar_autos(ventana)
        
        lbl_titulo=Label(ventana,text="..::Ingresa los siguientes datos del tipo auto ::..")
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
        Interfaz.buscar_autos(ventana)
        pass
    @staticmethod
    def mostrar_autos(ventana):
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador.mostrar_autos()
        if len(registro)>0:
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
    @staticmethod
    def camionetas_insertar(ventana):
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
        lbl_caballaje=Label(ventana,text="Caballaje")
        lbl_caballaje.pack(pady=10)
        etr_caballaje=Entry(ventana)
        etr_caballaje.pack(pady=5)
        lbl_plazas=Label(ventana,text="Plazas")
        lbl_plazas.pack(pady=10)
        etr_plazas=Entry(ventana)
        etr_plazas.pack(pady=5)
        lbl_traccion=Label(ventana,text="Tracción")
        lbl_traccion.pack(pady=10)
        etr_traccion=Entry(ventana)
        etr_traccion.pack(pady=5)
        lbl_cerrada=Label(ventana,text="Cerrada")
        lbl_cerrada.pack(pady=10)
        etr_cerrada=Entry(ventana)
        etr_cerrada.pack(pady=5)
        btn_ingres=Button(ventana,text="Insertar" ,command=lambda:controlador.Controlador_camionetas.registrar_camioneta("Camionetas",
                    etr_color.get(),
                    etr_marca.get(),
                    etr_modelo.get(),
                    etr_velocidad.get(),
                    etr_caballaje.get(),
                    etr_plazas.get(),
                    etr_traccion.get(),
                    etr_cerrada.get()))
        btn_ingres.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_autos(ventana))
        btn_regresar.pack()
    @staticmethod
    def camiones_insertar(ventana):
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
        lbl_caballaje=Label(ventana,text="Caballaje")
        lbl_caballaje.pack(pady=10)
        etr_caballaje=Entry(ventana)
        etr_caballaje.pack(pady=5)
        lbl_plazas=Label(ventana,text="Plazas")
        lbl_plazas.pack(pady=10)
        etr_plazas=Entry(ventana)
        etr_plazas.pack(pady=5)
        lbl_eje=Label(ventana,text="Eje")
        lbl_eje.pack(pady=10)
        etr_eje=Entry(ventana)
        etr_eje.pack(pady=5)
        lbl_capacidad=Label(ventana,text="capacidad")
        lbl_capacidad.pack(pady=10)
        etr_capacidad=Entry(ventana)
        etr_capacidad.pack(pady=5)
        btn_ingres=Button(ventana,text="Insertar" ,command=lambda:controlador.Controlador_camiones.registrar_camiones("Camiones",
                    etr_color.get(),
                    etr_marca.get(),
                    etr_modelo.get(),
                    etr_velocidad.get(),
                    etr_caballaje.get(),
                    etr_plazas.get(),
                    etr_eje.get(),
                    etr_capacidad.get()))
        btn_ingres.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_autos(ventana))
        btn_regresar.pack()
        pass
    @staticmethod
    def cambiar_camionetas(ventana):
        Interfaz.buscar_autos(ventana)
        Interfaz.borrarPantalla(ventana)
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
        btn_cambiar=Button(ventana,text="Cambiar" ,command="")
        btn_cambiar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
        pass
    @staticmethod
    def cambiar_camiones(ventana):
        Interfaz.buscar_autos(ventana)
        Interfaz.borrarPantalla(ventana)
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
        btn_cambiar=Button(ventana,text="Cambiar" ,command="")
        btn_cambiar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def borrar_camionetas(ventana):
        btn_borrar=Button(ventana,text="Borrar" ,command="")
        btn_borrar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
        pass
    @staticmethod
    def borrar_camiones(ventana):
        btn_borrar=Button(ventana,text="Borrar" ,command="")
        btn_borrar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def mostrar_camionetas(ventana):
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador.mostrar_autos()
        if len(registro)>0:
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def mostrar_camiones(ventana):
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador.mostrar_autos()
        if len(registro)>0:
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
