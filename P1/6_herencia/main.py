#instanciar los objetos para implementarlos después

from coches import *

coche=Coches("bm","blanco","sss",120,150,5)
print(coche.marca,coche.acelerar())

camioneta=Camionetas("bm","blanco","sss",120,150,5,"trasera",False)
print(camioneta.marca,camioneta.acelerar())

camion=Camiones("bm","blanco","sss",120,150,5,2,3000)
print(camion.marca,camion.acelerar())

# marca=input("Escribe la marca del auto: ").upper()
# color=input("Escribe el color del carro: ").upper()
# modelo=input("Escribe el modelo del carro: ").upper()
# velodidad=input("Escriba la velocidad del carro: ").upper()
# potencia=input("Escriba la potencia: ").upper()
# plazas=input("Escriba las plazas: ").upper()

# coche1=Coches(marca,color,modelo,velodidad,potencia,plazas)
# print(f"El coche 1 es un {coche1.get_marca()} de color {coche1.get_color()} y modelo {coche1.get_modelo()} con una velocidad maxima de {coche1.get_velocidad()} km/h  y una potencia de {coche1.get_caballaje()} caballos y tiene {coche1.get_plazas()} plazas")
# # coche2=Coches()
# # print(f"El coche 2 es un {coche2.get_marca()} de color {coche2.get_color()} y modelo {coche2.get_modelo()} con una velocidad maxima de {coche2.get_velocidad()} km/h  y una potencia de {coche2.get_caballaje()} caballos y tiene {coche2.get_plazas()} plazas")

