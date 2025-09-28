import os
os.system("cls")

class Coches:
    #Metodo constructor: con este metodo se inicializa un objeto cuando es creado con valores iniciales.
    def __init(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

#CRear los metodos setter y getter: estos metodos son importantes y necesarios en todas las clases para que el programador interactua 
#con los valores de los atributos a traves de estos metodos... digamos que es la manera mas adecuada y recomendada para solicitar un 
# valor (get)  y /0 para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.
# en teoria se deberia de crear un metodo Getter y Setter por cada atributo que contenga la clase.
# los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return 
# por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def get_marca(self):
        return self.__marca
    def set_marca(self,marca):
        self.__marca=marca
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self,modelo):
        self.__modelo=modelo
    def get_velocidad(self):
        return self.__velocidad
    def set_velocidad(self,velocidad):
        self.__velocidad=velocidad
    def get_caballaje(self):
        return self.__caballaje
    def set_caballaje(self,caballaje):
        self.__caballaje=caballaje
    def get_plazas(self):
        return self.__plazas
    def set_plazas(self,plazas):
        self.__plazas=plazas


    def acelerar(self,incremento):
        pass

    def frenar(self,decre):
        pass
    
coche1=Coches("BMW","Blanco","2022",220,150,5)
# coche1.set_marca("BMW")
# coche1.set_color("Blanco")
# coche1.set_modelo("2022")
# coche1.set_velocidad(220)
# coche1.set_caballaje(150)
# coche1.set_plazas(5)

# print(f"El coche 1 es un {coche1.get_marca()} de color {coche1.get_color()} y modelo {coche1.get_modelo()} con una velocidad maxima de {coche1.get_velocidad()} km/h  y una potencia de {coche1.get_caballaje()} caballos y tiene {coche1.get_plazas()} plazas")

coche2=Coches("KIA","Naranja","2021",140,200,7)
# coche2.set_marca("Nissan")
# coche2.set_color("Negro")
# coche2.set_modelo("2022")
# coche2.set_velocidad(120)
# coche2.set_caballaje(270)
# coche2.set_plazas(6)

# print(f"El coche 2 es un {coche2.get_marca()} de color {coche2.get_color()} y modelo {coche2.get_modelo()} con una velocidad maxima de {coche2.get_velocidad()} km/h  y una potencia de {coche2.get_caballaje()} caballos y tiene {coche2.get_plazas()} plazas")



