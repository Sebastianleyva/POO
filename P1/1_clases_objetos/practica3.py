import os
os.system("cls")

class Alumnos():
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def inscribirse(self):
        print("El alumno se ha inscrito :)")

    def estudiar(self):
        print("El alumno está estudiando :|")
        
alumno1=Alumnos("Juan Correa simental",25,100123)
print(f"{alumno1.inscribirse()}")
alumno2=Alumnos("Maria Serrano Mata",22,100124)
print(alumno2.estudiar())

class Cursos():
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar():
        pass

curso1=Cursos("POO",100,6)
curso2=Cursos("FOSO",101,4)

class Profesores():
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def impartir(self):
        pass
    def evaluar(self):
        print("El profesor está evaluando")

print("-"*60)
profesor1=Profesores("Ana Torres Guzman",20,123)
profesor2=Profesores("Daniel Contreras",35,124)
print(profesor1.evaluar())
