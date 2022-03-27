"""Ejercicio 6 
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:"""

def separar(lista1):#Se define la funcion separar con un parámetro de entrada lista
    lista_pares=[]#Se define la lista de numeros pares
    lista_impares=[]#Se define la lista de numeros impares
    for i in lista1:#Funcion for para clasificar los pares de impares
        if i%2==0:
            lista_pares.append(i)#Si el módulo del número para 2 es 0, se añade a la lista de pares
        else:
            lista_impares.append(i)#Caso contrario se añade los impares
    lista_pares.sort()#Se ordena las listas
    lista_impares.sort()
    print("Lista pares:",lista_pares,"\n","Lista impares:",lista_impares)#Se imprime el resultado

separar([-12, 84, 13, 20, -33, 101, 9])