"""Ejercicio 2
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio:"""
from math import pi#Se importa el valor pi de la biblioteca math

class Circulo:#Defino la clase Circulo
    def __init__ (self,radio):#Defino la función init con el atributo radio
        self.radious= radio
    def area_circulo(self):#Se define la función área de circulo
        area= pi*((self.radious)*(self.radious))#Se calcula el área del circulo a partir de los atributos dados
        print("Área de Círculo:",area)#Se imprime el área del circulo
        return area#Se retorna el valor del área

circulo1 = Circulo(5)#Se crea el objeto circulo 1
circulo1.area_circulo()#Se llama al atributo área del circulo