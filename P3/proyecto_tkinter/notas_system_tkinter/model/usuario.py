import conexionBD
import hashlib
import datetime


class Usuario:
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        try:
            
            fecha=datetime.datetime.now()
            conexionBD.cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellidos,email,hashlib.sha256(password.encode()).hexdigest(),fecha)
            )
            conexionBD.conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            conexionBD.cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=conexionBD.cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None         
        

