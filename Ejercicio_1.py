"""Ejercicio 1 Realiza una función llamada area_rectangulo() 
que devuelva el área del rectangulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura."""

class Rectangulo:#Defino la clase rectángulo
    def __init__ (self,base,altura):#Defino la función init con los atributos base y altura
        self.base= base
        self.height= altura
    def area_rectangulo(self):#Se define la función área de un rectángulo 
        area=self.base*self.height#Se calcula el área del rectángulo a partir de los atributos dados
        print("Área de Rectángulo:",area)#Se imprime el área del rectángulo
        return area#Se retorna el valor del área

rectangulo1 = Rectangulo(15,10)#Se crea el objeto rectángulo 1
rectangulo1.area_rectangulo()#Se llama al atributo área del rectángulo


