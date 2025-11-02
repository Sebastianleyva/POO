import hashlib
from datetime import datetime
import conexionBD

class Notas():
    def __init__(self,usuario_id,titulo,descripcion,fecha=None,id=None):
        self._id=id
        self._usuario_id=usuario_id
        self._titulo=titulo
        self._descripcion=descripcion
        self._fecha = fecha if fecha else datetime.now()

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id=id

    @property
    def usuario_id(self):
        return self._usuario_id
    @usuario_id.setter
    def usuario_id(self,usuario_id):
        self._usuario_id=usuario_id
    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,titulo):
        self._titulo=titulo
    
    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self,descripcion):
        self._descripcion=descripcion

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha):
        self._fecha=fecha

    def crear(self):
        try:
          conexionBD.cursor.execute(
            "insert into notas values(null,%s,%s,%s,NOW())",
            (self._usuario_id,self._titulo,self._descripcion)
          )
          conexionBD.conexion.commit()
          return True
        except:
          return False
        
    def mostrar(self):
        try:
          conexionBD.cursor.execute(
            "select * from notas where usuario_id=%s",
            (self._usuario_id,)
          )
          return conexionBD.cursor.fetchall()
        except:    
          return []
        
    def actualizar(self):
        try:
         conexionBD.cursor.execute(
            "update notas set titulo=%s,descripcion=%s where id=%s",
            (self._titulo,self._descripcion,self._id)
         )
         conexionBD.conexion.commit()
         return True
        except: 
         return False
        pass
    def eliminar(self):
        try:
          conexionBD.cursor.execute(
            "delete from notas where id=%s",
            (self._id,)
          ) 
          conexionBD.conexion.commit() 
          return True  
        except:    
          return False
        pass

class Usuarios():
    def __init__(self,nombre,apellido,email,contrasena,fecha=None,id=None):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._email=email
        self._password=contrasena
        self._fecha = fecha if fecha else datetime.now()
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id=id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email=email
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        self._password=password

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha):
        self._fecha=fecha
    def registrar(self):
        """Registra el usuario actual en la BD usando los atributos de la instancia.

        Retorna True si se insertó correctamente, False en caso de error.
        """
        try:
            hashed = hashlib.sha256(self._password.encode()).hexdigest()
            fecha = datetime.now()
            # usar el cursor exportado por view/conexionBD.py
            cursor = conexionBD.cursor
            cursor.execute(
                "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)",
                (self._nombre, self._apellido, self._email, hashed, fecha)
            )
            conexionBD.conexion.commit()
            return True
        except Exception as e:
            print("Error en registrar:", e)
            return False
    def iniciar_sesion(self):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor= conexionBD.cursor
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (self._email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None
