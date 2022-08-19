# Listas   ----IR DESCOMENTANDO EJERCICIO POR EJERCICIO SIN COMENTAR EL CÓDIGO DEL PUNTO 1----

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

num=int(input("Ingrese el número de palabras que quiere que contenga la lista: "))
lista=[]
for i in range(num):
    lista.append(input("Palabra: "))
		
print(f"La lista ingresada es: {lista}")

# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

# buscar= input("Ingrese la palabra que quiere buscar: ")
# aparece = lista.count(buscar)
# print(f"La palabra '{buscar}' aparece {aparece} veces en la lista: {lista}")


# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

# reemplazo= input("Ingrese la palabra que quiere cambiar: ")
# donde = lista.index(reemplazo)
# nueva= input("Ingrese la nueva palabra: ")
# lista.insert(donde, nueva)
# lista.remove(reemplazo)
# print(f"La lista elimino la palabra '{reemplazo}' y agrego la palabra '{nueva}', el resultado es: {lista}")


# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.


# eliminar = input("Ingrese la palabra que quiere eliminar: ")
# lista.remove(eliminar)
# print(f"Se elimino la palabra '{eliminar}' y lista quedo así: {lista}")


# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

# lista2= ["paco", "Lucia", "Ana", "Natali", "Martillo", "enchufe", "escritorio"]
# lista3=[]
# for i in lista:
#     if i in lista2:
#         lista.remove(i)
#         lista3.append(i)               
# print(f"la primer lista quedo asi: {lista}")
# print(f"El elemento '{i}' fue eliminado y se agrego a la segunda lista, resultado final: {lista3}")

# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).


# lista2 = lista[::-1]
# print(f"La primer lista quedo asi: {lista}")
# print(f"La segunda lista invertida quedo asi: {lista2}")

#----IR DESCOMENTANDO EJERCICIO POR EJERCICIO SIN COMENTAR EL CÓDIGO DEL PUNTO 1----