"""Ejercicios 4
Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
Comprueba el punto intermedio entre -12 y 24"""
def intermedio(n1,n2):#Se define la funcion intermedio
    inter=(n1+n2)/2
    return inter#Se devuelve el valor intermedio

print("Valor intermedio: ", intermedio(-12,24))#Se imprime el resultado de la función con los parámetros dados