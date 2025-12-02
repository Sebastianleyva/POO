from conexionBD import *
from tkinter import messagebox


class Operaciones():
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            cursor.execute(
                "insert into operaciones values(null,NOW(),%s,%s,%s,%s)",
                (numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("select * from operaciones")
            return cursor.fetchall()
        except:    
            return []
    
    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute(
                "update operaciones set numero1=%s,numero2=%s,signo=%s,resultado=%s where id=%s",
                (numero1,numero2,signo,resultado,id)
            )
            conexion.commit()
            return True
        except: 
            return False
    
    @staticmethod   
    def eliminar(id):
        if Operaciones.buscar(id) is None:
            return False
        else:
                try:
                    cursor.execute(
                        "delete from operaciones where id=%s",
                        (id,)
                    ) 
                    conexion.commit() 

                    return True  
                except:    
                    return False
        respuesta=""
        Operaciones.respuesta_sql("Eliminar Operación",respuesta)
        
    @staticmethod
    def buscar(id):
        try:
            cursor.execute("select * from operaciones where id=%s",(id,))
            return cursor.fetchone()
        except:
            return None

    @staticmethod
    def consultar(id):
        row = Operaciones.buscar(id)
        if row:
            try:
                return {
                    "id": row[0],
                    "fecha": row[1],
                    "numero1": row[2],
                    "numero2": row[3],
                    "signo": row[4],
                    "resultado": row[5]
                }
            except Exception:
                return None
        return None

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",message=f"Nota {titulo} actualizada correctamente")
        else:
            messagebox.showerror(icon="error",message=f"Error al actualizar la nota {titulo}, intentelo de nuevo")
