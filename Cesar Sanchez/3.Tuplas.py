# Practica de tuplas 

# *Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

""" tupla1 = (1, 2, 3)

tupla2 = (-1, 0, 2)

productoEscalar = 0

for i in range (len(tupla1)) :          # La cantidad de la tupla es 3 

    productoEscalar += tupla1[i] * tupla2 [i]           # Entro en cada tupla con [] y hago la múltiplicación de sus elementos.    A eso le voy sumando la siguiente multiplicación

print (f'El producto escalar de los vectores {tupla1} y {tupla2} es {productoEscalar}') """


# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

""" precios = (50, 75, 46, 22, 80, 65, 8)

minima = precios [0]         # Minima = tupla en la posición 0 de nuestra lista, que es 50

maxima = precios [0]         # Maxima = tupla en la posición 0 de nuestra lista, que es 50

for i in precios:   # Recorro los elementos de la lista precios

    if i < minima: 

        minima = i 

    elif i > maxima : 

        maxima = i 

print (f'El precio mínimo es:  {minima} y el precio máximo es {maxima}') """




# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

""" numeros = str (input("Cuantos números de su lista separados por coma: "))   

# print(numeros, " sin split")

numeros = numeros.split(',')      # Convierto a los números en string y me los PASA A UNA LISTA

print (numeros, " con el método split")

cantidad = len (numeros)       # La cantidad de elementos que se encuentra en la lista

for i in range(cantidad):

    numeros[i] = int (numeros[i])             #Convierto los números de string en un int

print ( numeros )


# Ahora hacemos las operaciones de estadística

sum = 0

elevadocuadrado = 0

for i in numeros:     # Recorro la lista 

    sum += i

    elevadocuadrado += i**2

promedio = sum / cantidad

desviacion = (elevadocuadrado/numeros-promedio**2)**(0.5)

print("La media es, ", promedio, "la desviación típica es ,",desviacion) """