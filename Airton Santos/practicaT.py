# Listas

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego 
# solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

# numero = int(input("Ingrese un numero"))

# def palabras ():
#     i = 0
#     listaPalabras = []
#     while i < numero: 
#         nuevaPalabra = input("Ingrese una palabra")
#         listaPalabras.append(nuevaPalabra)
#         i += 1 
#     print(listaPalabras)

# palabras()

# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas 
# veces aparece esa palabra en la lista.

# def listaPalabras():
#     listaVacia = []
#     i = 0

#     while i < 3:
#         palabra = input("Ingrese una palabra")
#         listaVacia.append(palabra)
#         i += 1 

#     coincidencia = input("Escriba una palabra para buscar")
#     contador = listaVacia.count(coincidencia)
#     print(f"La palabra {coincidencia} aparece {contador} veces ")

# listaPalabras()

# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la 
# primera por la segunda en la lista.


# def listaPalabras2():
#     listaVacia = []
#     i = 0

#     while i < 3:
#         palabra = input("Ingrese una palabra")
#         listaVacia.append(palabra)
#         i += 1 

#     palabra1 = input("Ingrese una palabra existente en la lista")
#     palabra2 = input("Ingrese una palabra para reemplazarla")

#     indice = listaVacia.index(palabra1)

#     listaVacia.insert(indice, palabra2)
#     listaVacia.remove(palabra1)

#     print(listaVacia)

# listaPalabras2()



# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

def listaPalabras3():
    listaVacia = []
    i = 0

    while i < 3:
        palabra = input("Ingrese una palabra")
        listaVacia.append(palabra)
        i += 1 
    palabra = input("Ingrese una palabra a eliminar")
    listaVacia.remove(palabra)
    print(listaVacia)

listaPalabras3()

# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres 
# de la segunda lista.

def listaPalabras4():

    lista1 = []
    lista2 = []
    i = 0
    x = 0 

    while i < 3:
        palabra = input("Ingrese una palabra para la lista1")
        lista1.append(palabra)
        i += 1

    
    while x < 3:
        palabra = input("Ingrese una palabra para la lista2")
        lista2.append(palabra)
        x += 1

    for i in lista1:
        for x in lista2:
            if i == x:
                lista1.remove(i)

    print(lista1)
                    

listaPalabras4()

# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, 
# pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

def listaPalabras5():
    listaVacia = []
    listaNueva = []
    i = 0

    while i < 3:
        palabra = input("Ingrese una palabra")
        listaVacia.append(palabra)
        i += 1

    listaNueva = listaVacia[::-1]

    print(listaNueva)

listaPalabras5()