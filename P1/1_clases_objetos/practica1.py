#Crear un programa que calcule el area de un rectangulo
import os

base=6
altura=10
def area(base,altura):
    area=base*altura
    return area

area=area()
print(f"el area es: {area}")

#POO

class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def areaRectangulo(self):
        area=self.base*self.altura
        return area
rectangulo=AreaRectangulo(10,6)#Instanciar el area de un rectangulo con una clase
print(f"El area del rectangulo es: {rectangulo.areaRectangulo()}")