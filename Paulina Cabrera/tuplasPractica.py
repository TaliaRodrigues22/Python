# Practica de tuplas 
# *Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

# vectorA = (1,2,3)
# vectorB = (-1,0,2)

# listaVectorA = []
# listaVectorB = []

# listaVectorA.append(vectorA)
# listaVectorB.append(vectorB)

# producto = 0
# for i in range(len(vectorA)):
#     producto += vectorA[i] * vectorB[i]
# print(f"El producto de los vectores {listaVectorA} y {listaVectorB} es = {producto}")

# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# listaPrecios = [ 50, 75, 46, 22, 80, 65, 8]

# peque = min(listaPrecios)
# grande = max(listaPrecios)
# print(f"El menor precio de la lista {listaPrecios} es: {peque} y el mayor es: {grande}")

# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


numeros = input("Ingrese numeros: ")
numeros = numeros.split(',')
cantidad= len(numeros)
for i in range(cantidad):
    numeros[i] = int(numeros[i])
print(f"La lista de números ingresada es: {numeros}")
suma = sum(numeros)
media = suma / cantidad
suma2 = 0
for i in numeros:
    suma2 += i**2
desvTip = (suma2/ cantidad - media**2)** (1/2)
print(f"La media de la lista {numeros} es igual a: {media} y la desviación típica es igual a: {desvTip}")


