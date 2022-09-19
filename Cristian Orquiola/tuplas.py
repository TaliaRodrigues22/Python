# Practica de tuplas 
# Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

vector1 = (1,2,3)
vector2 = (-1,0,2)

mult1 = vector1[0] * vector2[0]
mult2 = vector1[1] * vector2[1]
mult3 = vector1[2] * vector2[2]

suma = mult1 + mult2 + mult3

print(vector1)
print(vector2)
print(suma)

# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = (50, 75, 46, 22, 80, 65, 8)

minimo = min(precios)
maximo = max(precios)

print("el numero menor es: ",minimo, " el numero maximo es: ",maximo)

# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

