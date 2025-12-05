from view import interfaz
from tkinter import messagebox
import conexionBD
from model import modelo_carro

class Controlador_autos:
    @staticmethod
    def registrar_auto(titulo,color,marca,modelo, velocidad,caballaje,plazas,id=None):
        resultado=modelo_carro.Modelo_carro.registrar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def mostrar_autos(id):
        resultado=modelo_carro.Modelo_carro.mostrar_autos(id)
        Controlador_autos.respuesta_sql("mostrar",resultado)
        return resultado
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",message=f"coche {titulo} actualizado correctamente")
        else:
            messagebox.showerror(icon="error",message=f"Error al actualizar el coche {titulo}, intentelo de nuevo")
    @staticmethod
    def eliminar_auto(titulo,id):
        resultado=modelo_carro.Modelo_carro.eliminar(id)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def buscar_auto(id):
        resultado=modelo_carro.Modelo_carro.buscar(id)
        return resultado
    @staticmethod
    def actualizar_auto(titulo,color,marca,modelo, velocidad,caballaje,plazas,id):
        resultado=modelo_carro.Modelo_carro.actualizar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql("Actualizado",resultado)

class Controlador_camionetas():
    #por corregir 
    @staticmethod
    def registrar_camionetas(titulo,color,marca,modelo, velocidad,caballaje,plazas,id=None):
        resultado=modelo_carro.Modelo_carro.registrar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def mostrar_camionetas():
        resultado=modelo_carro.Modelo_carro.mostrar_autos()
        Controlador_autos.respuesta_sql("mostrar",resultado)
        return resultado
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",message=f"coche {titulo} actualizado correctamente")
        else:
            messagebox.showerror(icon="error",message=f"Error al actualizar el coche {titulo}, intentelo de nuevo")
    @staticmethod
    def eliminar_auto(titulo,id):
        resultado=modelo_carro.Modelo_carro.eliminar(id)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def buscar_auto(id):
        resultado=modelo_carro.Modelo_carro.buscar(id)
        return resultado
    @staticmethod
    def actualizar_auto(titulo,color,marca,modelo, velocidad,caballaje,plazas,id):
        resultado=modelo_carro.Modelo_carro.actualizar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql("Actualizado",resultado)

class Controlador_camiones():
    @staticmethod
    def registrar_camiones(titulo,color,marca,modelo, velocidad,caballaje,plazas,id=None):
        resultado=modelo_carro.Modelo_carro.registrar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def mostrar_camiones():
        resultado=modelo_carro.Modelo_carro.mostrar_autos()
        Controlador_autos.respuesta_sql("mostrar",resultado)
        return resultado
    @staticmethod
    def respuesta_camiones(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",message=f"coche {titulo} actualizado correctamente")
        else:
            messagebox.showerror(icon="error",message=f"Error al actualizar el coche {titulo}, intentelo de nuevo")
    @staticmethod
    def eliminar_camiones(titulo,id):
        resultado=modelo_carro.Modelo_carro.eliminar(id)
        Controlador_autos.respuesta_sql(titulo,resultado)
    @staticmethod
    def buscar_camiones(id):
        resultado=modelo_carro.Modelo_carro.buscar(id)
        return resultado
    @staticmethod
    def actualizar_camiones(titulo,color,marca,modelo, velocidad,caballaje,plazas,id):
        resultado=modelo_carro.Modelo_carro.actualizar(id,color,marca,modelo, velocidad,caballaje,plazas)
        Controlador_autos.respuesta_sql("Actualizado",resultado)