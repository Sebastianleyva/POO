from tkinter import *
from tkinter import messagebox
from controller import controlador

class MenuPrincipal:
    def __init__(self, ventana):
        self.Menu_principal(ventana)
    
    @staticmethod
    def limpiar(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def Menu_principal(ventana):
        MenuPrincipal.limpiar(ventana)
        Label(ventana, text=".:: Menu Principal ::.", font=("Arial", 16)).pack(pady=20)
        Button(ventana, text="Registro",width=12, command=lambda: MenuPrincipal.Registro(ventana)).pack(pady=10)
        Button(ventana, text="Login",width=12, command=lambda: MenuPrincipal.iniciar_sesion(ventana)).pack(pady=10)
        Button(ventana, text="Salir",width=12, command=ventana.destroy).pack(pady=20)
    
    @staticmethod
    def Registro(ventana):
        MenuPrincipal.limpiar(ventana)
        Label(ventana, text=".::Registro en el sistema ::.", font=("Arial", 16)).pack(pady=10)
        Label(ventana, text="¿Cual es tu nombre?:").pack(pady=5)
        txt_nombre=Entry(ventana, width=30)
        txt_nombre.pack(pady=5)
        Label(ventana, text="¿Cuáles son tus apellidos?:").pack(pady=5)
        txt_apellidos=Entry(ventana, width=30)
        txt_apellidos.pack(pady=5)
        Label(ventana, text="Ingresa tu email:").pack(pady=5)
        txt_email=Entry(ventana, width=30)
        txt_email.pack(pady=5)
        Label(ventana, text="Ingresa tu Contraseña:").pack(pady=5)
        txt_password=Entry(ventana, width=30, show="*")
        txt_password.pack(pady=5)
        btn_registro=Button(ventana, text="Registrar", width=12,command=lambda: controlador.Controlador.registrar(txt_nombre.get(), txt_apellidos.get(), txt_email.get(), txt_password.get()))
        btn_registro.pack(pady=10)
        Button(ventana, text="Volver", width=12,command=lambda: MenuPrincipal.Menu_principal(ventana)).pack(pady=5)
    
    @staticmethod
    def iniciar_sesion(ventana):
        MenuPrincipal.limpiar(ventana)
        Label(ventana, text=".:: Inicio de Sesión ::.", font=("Arial", 16)).pack(pady=10)
        Label(ventana, text="Ingresa tu email:").pack(pady=5)
        txt_email=Entry(ventana, width=30)
        txt_email.pack(pady=5)
        Label(ventana, text="Ingresa tu Contraseña:").pack(pady=5)
        txt_password=Entry(ventana, width=30, show="*")
        txt_password.pack(pady=5)
        Button(ventana, text="Entrar", width=12,command=lambda: {(controlador.Controlador.iniciar_sesion(txt_email.get(),txt_password.get(),ventana))}).pack(pady=10)
        Button(ventana, text="Volver", width=12,command=lambda: MenuPrincipal.Registro(ventana)).pack(pady=5)

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        MenuPrincipal.limpiar(ventana)
        global id_user, nom_usuario, ape_usuario
        id_user=usuario_id
        nom_usuario=nombre
        ape_usuario=apellidos
        lbl_tit=Label(ventana,text=f"..::Menú de notas de {nombre} {apellidos}::..",font=("Arial",16))
        lbl_tit.pack(pady=10)
        btn1=Button(ventana,text="crear",command=lambda: MenuPrincipal.Crear_notas(ventana,id_user))
        btn1.pack(pady=5)
        btn2=Button(ventana,text="Mostrar",command=lambda: MenuPrincipal.Mostrar_nota(ventana,id_user))
        btn2.pack(pady=5)
        btn3=Button(ventana,text="Cambiar",command=lambda: MenuPrincipal.Actualizar(ventana,id_user))
        btn3.pack(pady=5)
        btn4=Button(ventana,text="Eliminar",command=lambda: MenuPrincipal.Borrar_nota(ventana,id_user))
        btn4.pack(pady=5)
        btn5=Button(ventana,text="Regresar",command=lambda: MenuPrincipal.iniciar_sesion(ventana))
        btn5.pack(pady=5)
    
    @staticmethod
    def Crear_notas(ventana,id_user):
        MenuPrincipal.limpiar(ventana)
        lbl_tit=Label(ventana,text=f"{nom_usuario} {ape_usuario}, vamos a crear notas", justify="center")
        lbl_tit.pack(pady=10)
        lbl_2=Label(ventana,text="Titulo")
        lbl_2.pack(pady=5)
        txt_tit=Entry(ventana)
        txt_tit.pack(pady=5)
        lbl_3=Label(ventana,text="Descripción")
        lbl_3.pack(pady=5)
        txt_desc=Entry(ventana)
        txt_desc.pack(pady=5)
        btn_save=Button(ventana,text="Guardar",command=lambda: controlador.Controlador.crear_nota(id_user,txt_tit.get(),txt_desc.get()))
        btn_save.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda: MenuPrincipal.menu_notas(ventana,id_user,nom_usuario,ape_usuario))
        btn_volver.pack(pady=5)
    
    @staticmethod
    def Mostrar_nota(ventana,id_user):
        MenuPrincipal.limpiar(ventana)
        lbl_tit=Label(ventana,text=f"{nom_usuario} {ape_usuario}, tus notas son:", justify="center")
        lbl_tit.pack(pady=10)

        filas=""
        registro=controlador.Controlador.mostrar_notas(id_user)
        if len(registro)>0:
            num_notas=1
            for fila in registro:
                filas+=f"\nNota: {num_notas} \nID: {fila[0]}, Titulo: {fila[2]} \n Fecha creación: {fila[4]} Descrición: {fila[3]}"
                num_notas += 1
        else:
            messagebox.showinfo(icon="info",message="Valió madre este pedo")
        lbl_res=Label(ventana,text=f"{filas}")
        lbl_res.pack(pady=5)

        btn_vol=Button(ventana,text="Volver",command=lambda: MenuPrincipal.menu_notas(ventana,id_user,nom_usuario,ape_usuario))
        btn_vol.pack(pady=5)
    
    @staticmethod
    def Actualizar(ventana,id_user):
        MenuPrincipal.limpiar(ventana)
        lbl_tit=Label(ventana,text=f"..::{nom_usuario} {ape_usuario} vamos a modificar una nota::..")
        lbl_tit.pack(pady=10)
        lbl_2=Label(ventana,text="ID de la nota a cambiar")
        lbl_2.pack(pady=5)
        txt_ID=Entry(ventana)
        txt_ID.pack(pady=5)
        lbl_nuevo=Label(ventana,text="Nuevo titulo")
        lbl_nuevo.pack(pady=5)
        txt_nuevo=Entry(ventana)
        txt_nuevo.pack(pady=5)
        lbl_3=Label(ventana,text="Nueva descripción")
        lbl_3.pack(pady=5)
        txt_desc=Entry(ventana)
        txt_desc.pack(pady=5)
        btn_save=Button(ventana,text="Guardar", command=lambda: controlador.Controlador.actualizar(txt_ID.get(),txt_nuevo.get(),txt_desc.get()))
        btn_save.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda: MenuPrincipal.menu_notas(ventana,id_user,nom_usuario,ape_usuario))
        btn_volver.pack(pady=5)
    
    @staticmethod
    def Borrar_nota(ventana,id_user):
        MenuPrincipal.limpiar(ventana)
        lbl_tit=Label(ventana,text=f"..::{nom_usuario} {ape_usuario} vamos a borrar una nota::..")
        lbl_tit.pack(pady=10)
        lbl_2=Label(ventana,text="ID de la nota a borrar")
        lbl_2.pack(pady=5)
        txt_ID=Entry(ventana)
        txt_ID.pack(pady=5)

        btn_save=Button(ventana,text="Borrar",command=lambda: controlador.Controlador.eliminar(txt_ID.get()))
        btn_save.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda: MenuPrincipal.menu_notas(ventana,id_user,nom_usuario,ape_usuario))
        btn_volver.pack(pady=5)

        