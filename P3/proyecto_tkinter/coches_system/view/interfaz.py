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
        if tipo=="Autos":
            lbl_tit=Label(ventana,text=f"..:: Menú de {tipo} ::..",font=("Arial",16))
            lbl_tit.pack(pady=10)
            btn_insertar=Button(ventana,text="Insertar",command=lambda: Interfaz.autos_insertar(ventana))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="Consutltar",command=lambda: Interfaz.mostrar_autos(ventana))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="Actualizar",command=lambda: Interfaz.cambiar_autos(ventana))
            btn_actualizar.pack(pady=10)
            btn_Eliminar=Button(ventana,text="Eliminar",command=lambda: Interfaz.borrar_autos(ventana))
            btn_Eliminar.pack(pady=10)
        elif tipo=="Camionetas":
            lbl_tit=Label(ventana,text=f"..:: Menú de {tipo} ::..",font=("Arial",16))
            lbl_tit.pack(pady=10)
            btn_insertar=Button(ventana,text="Insertar",command=lambda: Interfaz.camionetas_insertar(ventana))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="Consutltar",command=lambda: Interfaz.mostrar_camionetas(ventana))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="Actualizar",command=lambda: Interfaz.cambiar_camionetas(ventana))
            btn_actualizar.pack(pady=10)
            btn_Eliminar=Button(ventana,text="Eliminar",command=lambda: Interfaz.borrar_camionetas)
            btn_Eliminar.pack(pady=10)
        elif tipo=="Camiones":
            lbl_tit=Label(ventana,text=f"..:: Menú de {tipo} ::..",font=("Arial",16))
            lbl_tit.pack(pady=10)
            btn_insertar=Button(ventana,text="Insertar",command=lambda: Interfaz.camiones_insertar(ventana))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="Consutltar",command=lambda: Interfaz.mostrar_camiones(ventana))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="Actualizar",command=lambda: Interfaz.cambiar_camiones(ventana))
            btn_actualizar.pack(pady=10)
            btn_Eliminar=Button(ventana,text="Eliminar",command=lambda: Interfaz.borrar_camiones(ventana))
            btn_Eliminar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def autos_insertar(ventana):
        Interfaz.borrarPantalla(ventana)
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        btn_ingres=Button(ventana,text="Insertar" ,command=lambda:controlador.Controlador_autos.registrar_auto("Autos",
                    etr_color.get(),
                    etr_marca.get(),
                    etr_modelo.get(),
                    etr_velocidad.get(),
                    etr_caballaje.get(),
                    etr_plazas.get()))
        btn_ingres.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana,"Autos"))
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
        btn_buscar=Button(ventana,text="Buscar",command=lambda: {on_buscar(),controlador.Controlador_autos.buscar_auto(txt_id.get())})
        btn_buscar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana,"Autos"))
        btn_regresar.pack()
        
    @staticmethod
    def cambiar_autos(ventana):
        Interfaz.buscar_autos(ventana)
        
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        btn_cambiar=Button(ventana,text="Cambiar" ,command="")
        btn_cambiar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana,"Autos"))
        btn_regresar.pack(pady=10)
    @staticmethod
    def borrar_autos(ventana):
        Interfaz.buscar_autos(ventana)

        pass
    @staticmethod
    def mostrar_autos(ventana):
        Interfaz.buscar_autos(ventana)
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador_autos.mostrar_autos(id)
        if len(registro)>0:
            filas=""
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana,"Autos"))
        btn_regresar.pack(pady=10)
    @staticmethod
    def camionetas_insertar(ventana):
        Interfaz.borrarPantalla(ventana)
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        lbl_traccion=Label(ventana,text="Tracción")
        lbl_traccion.grid(row=6,column=0,pady=5,padx=5)
        etr_traccion=Entry(ventana)
        etr_traccion.grid(row=6,column=1,pady=5,padx=5)
        lbl_cerrada=Label(ventana,text="Cerrada")
        lbl_cerrada.grid(row=7,column=0,pady=5,padx=5)
        etr_cerrada=Entry(ventana)
        etr_cerrada.grid(row=7,column=1,pady=5,padx=5)
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
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        lbl_eje=Label(ventana,text="Eje")
        lbl_eje.grid(row=6,column=0,pady=5,padx=5)
        etr_eje=Entry(ventana)
        etr_eje.grid(row=6,column=1,pady=5,padx=5)
        lbl_capacidad=Label(ventana,text="Capacidad")
        lbl_capacidad.grid(row=7,column=0,pady=5,padx=5)
        etr_capacidad=Entry(ventana)
        etr_capacidad.grid(row=7,column=1,pady=5,padx=5)
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
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        lbl_traccion=Label(ventana,text="Tracción")
        lbl_traccion.grid(row=6,column=0,pady=5,padx=5)
        etr_traccion=Entry(ventana)
        etr_traccion.grid(row=6,column=1,pady=5,padx=5)
        lbl_cerrada=Label(ventana,text="Cerrada")
        lbl_cerrada.grid(row=7,column=0,pady=5,padx=5)
        etr_cerrada=Entry(ventana)
        etr_cerrada.grid(row=7,column=1,pady=5,padx=5)
        btn_cambiar=Button(ventana,text="Cambiar" ,command="")
        btn_cambiar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_principal(ventana))
        btn_regresar.pack(pady=10)
        pass
    @staticmethod
    def cambiar_camiones(ventana):
        marco=Frame(ventana)
        marco.pack()
        lbl_marca=Label(marco,text="Marca")
        lbl_marca.grid(row=0,column=0,pady=5,padx=5)
        etr_marca=Entry(marco)
        etr_marca.grid(row=0,column=1,pady=5,padx=5)
        lbl_color=Label(marco,text="Color")
        lbl_color.grid(row=1,column=0,pady=5,padx=5)
        etr_color=Entry(marco)
        etr_color.grid(row=1,column=1,pady=5,padx=5)
        lbl_modelo=Label(marco,text="Mdelo")
        lbl_modelo.grid(row=2,column=0,pady=5,padx=5)
        etr_modelo=Entry(marco)
        etr_modelo.grid(row=2,column=1,pady=5,padx=5)
        lbl_velocidad=Label(marco,text="Velocidad")
        lbl_velocidad.grid(row=3,column=0,pady=5,padx=5)
        etr_velocidad=Entry(marco)
        etr_velocidad.grid(row=3,column=1,pady=5,padx=5)
        lbl_caballaje=Label(marco,text="Caballaje")
        lbl_caballaje.grid(row=4,column=0,pady=5,padx=5,)
        etr_caballaje=Entry(marco)
        etr_caballaje.grid(row=4,column=1,pady=5,padx=5)
        lbl_plazas=Label(marco,text="Plazas")
        lbl_plazas.grid(row=5,column=0,pady=5,padx=5)
        etr_plazas=Entry(marco)
        etr_plazas.grid(row=5,column=1,pady=5,padx=5)
        lbl_eje=Label(ventana,text="Eje")
        lbl_eje.grid(row=6,column=0,pady=5,padx=5)
        etr_eje=Entry(ventana)
        etr_eje.grid(row=6,column=1,pady=5,padx=5)
        lbl_capacidad=Label(ventana,text="Capacidad")
        lbl_capacidad.grid(row=7,column=0,pady=5,padx=5)
        etr_capacidad=Entry(ventana)
        etr_capacidad.grid(row=7,column=1,pady=5,padx=5)
        btn_cambiar=Button(ventana,text="Cambiar" ,command="")
        btn_cambiar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def borrar_camionetas(ventana):
        btn_borrar=Button(ventana,text="Borrar" ,command="")
        btn_borrar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana))
        btn_regresar.pack(pady=10)
        pass
    @staticmethod
    def borrar_camiones(ventana):
        btn_borrar=Button(ventana,text="Borrar" ,command="")
        btn_borrar.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def mostrar_camionetas(ventana):
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador.mostrar_autos()
        if len(registro)>0:
            filas=""
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana))
        btn_regresar.pack(pady=10)
    @staticmethod
    def mostrar_camiones(ventana):
        lbl_titulo=Label(ventana,text="..:: Auto encontrado ::..",font=("Arial",16))
        lbl_titulo.pack(pady=10)
        registro=controlador.Controlador.mostrar_autos()
        if len(registro)>0:
            filas=""
            for fila in registro:
                filas+=f"\nID: {fila[0]} \nColor: {fila[1]}, Marca: {fila[2]} \nModelo: {fila[3]} Velocidad: {fila[4]} \nCaballaje: {fila[5]} Plazas: {fila[6]}\n"
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)
        btn_regresar=Button(ventana,text="Regresar",command=lambda: Interfaz.menu_acciones(ventana))
        btn_regresar.pack(pady=10)
