# # Practica de tuplas 
# *Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def vectores():
    vect1 = (1, 2, 3)
    vect2 = (-1, 0, 2)

    for i in vect1:
        for x in vect2:

            producto = i * x

    print(producto)

vectores()

# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

def precios():
    listaPrecios = (50, 75, 46, 22, 80, 65, 8)
    maximo = max(listaPrecios)
    minimo = min(listaPrecios)
    print(f"El precio mínimo es {minimo} y el precio máximo es {maximo}")

precios()

# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

def muestra():

    listaVacia = []
    i = 0
    sumaCuadrados = 0 

    while i < 5:
        numero = input("Ingrese varios números")
        listaVacia.append(int(numero))
        i += 1
        sumaCuadrados += i**2

    media = sum(listaVacia)/len(listaVacia)
    
    print(media)
muestra()