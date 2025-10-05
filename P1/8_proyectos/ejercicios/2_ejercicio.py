"""Realizar un programa el cual se declaren dos valores enteros por teclado utilizando el 
metodo __init__. Calcular despues la suma, resta, multiplicacion y división.
Utilizar un metodo para cada uno e imprimir los resultados obtenidos. LLamar a la clase Calculadora"""

import os
os.system("cls")

class Calculadora:
    def __init__(self,operando1,operando2):
        self._operando1=operando1
        self._operando2=operando2
    @property
    def operando1(self):
        return self._operando1
    @operando1.setter
    def operando1(self,operando1):
        self.operando1=operando1
    @property
    def operando2(self):
        return self._operando2
    @operando2.setter
    def operando2(self,operando2):
        self.operando2=operando2

    def sumar(self):
        suma=self._operando1+self._operando2
        return suma

    def restar(self):
        resta=self._operando2-self._operando1
        return resta
    
    def multiplicar(self):
        multi=self._operando1*self._operando2
        return multi
    
    def dividir(self):
        divide=self._operando1/self._operando2
        return divide
    
n1=int(input("numero: "))
n2=int(input("numero: "))
objeto1=Calculadora(n1,n2)
print(f"La suma de los atributos del objeto 1 es: {objeto1.sumar()}")
print(f"La resta es de {objeto1.restar()}")
print(f"La multiplicacion es: {objeto1.multiplicar()}")
print(f"La divison es: {objeto1.dividir()}")

class calculador():
    def __init__(self):
        self._n1=int(input("Escriba un numero"))
        self._n2=int(input("Escriba otro"))