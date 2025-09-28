import os
os.system("cls")

class Coches:
    def __init__(self,color,marca,velocidad):
        #atributos del futuro objeto
        self.__color=color 
        self.__marca=marca
        self.__velocidad=velocidad
#Metodos o acciones del objeto
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
        
    def frenar(self,decremento):
        self.__velocidad-=decremento
        return self.__velocidad
    
    def coar_claxon(self):
        print(f"pi")

#Instanciar los objetos
coche1=Coches("Blanco","Ford",220)
coche2=Coches("Naranja","KIA",140)

print(f"Los valores del primer objeto son: {coche1.__marca},{coche1.__color},{coche1.__velocidad}")
print(f"EL coche uno acelero de {coche1.__velocidad} a {coche1.acelerar(60)}")
print(f"Los valores del segundo objeto son: {coche2.__marca},{coche2.__color},{coche2.__velocidad}")
velocidad=coche2.frenar(50)
print(f"El cohce dos desaceleró {velocidad}")
