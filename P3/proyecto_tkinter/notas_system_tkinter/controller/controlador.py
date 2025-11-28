from tkinter import *
from tkinter import messagebox
from model import usuario,nota
import conexionBD
from view import menu_principal

class Controlador():

    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registró correctamente con el email: {email}")
        else:
            messagebox.showerror(icon="error",message="Intentelo de nuevo, error en el sistema")

    @staticmethod
    def iniciar_sesion(email,password,ventana):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f"Bienvenido al sistema {registro[1]} {registro[2]}")
            menu_principal.MenuPrincipal.menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showerror(icon="error",message="Error al iniciar sesión, verifique sus datos")

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",message=f"Nota {titulo} actualizada correctamente")
        else:
            messagebox.showerror(icon="error",message=f"Error al actualizar la nota {titulo}, intentelo de nuevo")

    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        resultado=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql(titulo,resultado)

    @staticmethod
    def mostrar_notas(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    
    @staticmethod
    def eliminar(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Borrar Notas",respuesta)
    
    @staticmethod
    def actualizar(id,titulo,descripcion):
        resultado=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql(titulo,resultado)