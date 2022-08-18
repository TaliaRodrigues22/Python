# Listas

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
num=int(input("Ingrese un numero: "))
lista=[]
for i in range(num):
    palabra=input("Ingrese una palabra: ")
    lista.append(palabra)
print(lista)

# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
lista2=["violeta","lila","esmeralda","rosa"]
p=input("Ingrese una palabra: ").lower()
n=lista2.count(p)

print(lista2)
print("La palabra ", p, " aparece ", n, " veces.")

# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
primerPalabra=input("Ingrese una palabra existente: ")
segundaPalabra=input("Ingrese una palabra sustituyente: ")
indice=lista2.index(primerPalabra)
lista.remove(primerPalabra)
lista2.insert(indice,segundaPalabra)
print(lista2)

# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
palabra=input("Ingrese una palabra: ")
if palabra in lista:
    lista.remove(palabra)
print(lista)

# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
for i in lista:
    if i in lista2:
        lista.remove(i)
print(lista)

# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
listaCopy=lista.copy()
lista.reverse()
print(lista)