"""Ejercicio 3 
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'"""
def relacion (n1,n2):#Se define la funcion realcion con dos parámetros de entrada
    if n1>n2:#Si el número 1 es mayor al número 2 devuelve 1
        return 1
    elif n1<n2:#Si el número 1 es menor al número 2 devuelve -1
        return -1
    else:#Si el número 1 es igual al número 2 devuelve 0
        return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))