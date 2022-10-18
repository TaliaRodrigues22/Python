# # Practica de tuplas 
# *Realizar los 3 ejercicios con tuplas

#1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
a = (1,2,3)
b = (-1,0,2)

i, suma = 0, 0
while i < len(b):
    suma += a[i] * b[i]
    i += 1

print(f"El producto escalar entre {a} y {b} es: {suma}")


# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios = (50, 75, 46, 22, 80, 65, 8)
max, min = 0, precios[0]

for x in precios:
    if x > max:
        max = x
    elif x < min:
        min = x

print(f"El menor de lista es {min} y maximo es {max}")


# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
numString = input("Ingrese una muestra de numeros: ")

numTuple = tuple(map(int, numString.split(", ")))
media = 0
contador = 0
#iterar para media
for x in numTuple:
    media += x
media = media / len(numTuple)
#Iterar para varianza
for i in numTuple:
    contador += (i - media)**2
varianza = contador / len(numTuple)
#Desviacion tipica
desviacion = varianza**0.5 

print(f"La media: {media} y desviacion tipica: {desviacion} de la tupla: {numTuple}")
