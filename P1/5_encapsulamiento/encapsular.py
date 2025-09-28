#Encampsular: es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una 
# clase a la hora de usar un objeto o en herencia

import os 
os.system("cls")

class clase: 
    atributo_publico="Soy un atributo pyblico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamano):
        self._color=color
        self._tamano=tamano

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color

    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self,tamano):
        self._tamano=tamano

    @property
    def atributo_public(self):
        return self.atributo_publico
    @atributo_public.setter
    def atributo_public(self,atributo_publico):
        self.atributo_publico=atributo_publico
    
    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    @atributo_protegido.setter
    def atributo_protegido(self,atributo_protegido):
        self._atributo_protegido=atributo_protegido
    
    @property
    def atributo_privado(self):
        return self.__atributo_privado
    @atributo_privado.setter
    def atributo_privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

    # def getAtributoPrivado(self):
    #     return self.__atributo_privado

objeto=clase("Rojo","Grande")
#mala practica porque se accede directamente a los atributos y eso no es recomendable porque se pierde el control de los valores
#ademas de que si se cambia el nombre del atributo en la clase, el codigo que lo usa se rompe
#print(objeto.atributo_publico) #se puede acceder sin problema
#print(objeto._atributo_protegido) #se puede acceder pero no es recomendable
#print(objeto.__atributo_privado) #no se puede acceder, marca error
print(objeto.atributo_privado) #se accede a traves de un metodo publico que retorna el valor del atributo privado
print(objeto.atributo_publico)
print(objeto.atributo_protegido)

#Este programa no funciona porque el metodo constructor tiene un error, le falta un guion bajo en el nombre del metodo
#ademas de que no se estan usando los metodos getter y setter para acceder a los atributos privados
#por lo que no se puede acceder a los atributos privados desde fuera de la clase

#El error que marca en el atributo publico es porque se esta intentando acceder a un atributo que no existe, ya que el atributo publico
#se llama atributo_publico y no atributo publico, ademas de que se esta intentando acceder directamente al atributo y no a traves
# de un metodo getter

#Al tratar de imprimir el atributo publico, nos econtramos con un error, aunque el atributo exista en la linea siguiente de la clase, esto es 
#porque en la clase se esta intentando acceder a un atributo que no existe, ya que el atributo publico se llama atributo_publico y no atributo publico, ademas de que se esta intentando acceder directamente al atributo y no a traves de un metodo getter


