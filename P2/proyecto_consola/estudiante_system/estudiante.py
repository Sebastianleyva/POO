"""
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Estudiante:
    def _init_(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    @property
    def nombre(self):
        return self._nombre  
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre  

    @property
    def nota(self):
        return self._nota 

    @nota.setter
    def nota(self,nota):
        self._nota=nota  
    
    def imprimir(self):
        print(f"El nombre del Estudiante es: {self.nombre} y su nota es: {self.nota}")

    def mostrar(self):
        if self.nota>=7:
            print("Si ha aprobado la nota")
        else:
            print("No ha aprobado la nota")


estudiante=Estudiante("Juan Diaz",7)
estudiante.imprimir()
estudiante.mostrar()