"""Ejercicio 5
Realiza una función llamada recortar() que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10"""

def recortar(num,lim_inf,lim_sup):#Defino la funcion recortar, cuyos parámetros de entrada son el número, el límite inferior, límite superior
    if num<lim_inf:#Si el numero es menor al límite inferior, se devuelve el límite inferior
        return lim_inf
    elif num>lim_sup:#Si el numero es mayor al límite superior, se devuelve el límite superior
        return lim_sup
    else:#Caso contrario, se devuelve el mismo número
        return num

print("Resutado: ",recortar(15,0,10))#Se imprime el resultado de la funcion 