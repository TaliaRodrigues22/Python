# Listas 

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

# num=int(input("Ingrese el número de palabras que quiere que contenga la lista:"))
# lista=[]
# for i in range(0,num+1):
#     lista.append(input("Palabra: "))
		
#print(f"La lista ingresada es: {lista}")
# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.


# num=int(input("Número de palabras:"))
# lista=[]
# for i in range(1,num+1):
#     lista.append(input("Palabra:"))
# print(f"La lista ingresada es: {lista}")
# buscar= input("Ingrese la palabra que quiere buscar: ")
# aparece = lista.count(buscar)


# print(f"La palabra '{buscar}' aparece {aparece} veces en la lista: {lista}")


# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

# num=int(input("Número de palabras:"))
# lista=[]
# for i in range(1,num+1):
#     lista.append(input("Palabra:"))
# print(f"La lista ingresada es: {lista}")
# reemplazo= input("Ingrese la palabra que quiere cambiar: ")
# donde = lista.index(reemplazo)
# nueva= input("Ingrese la nueva palabra: ")
# lista.insert(donde, nueva)
# lista.remove(reemplazo)
# print(f"La lista elimino la palabra {reemplazo} y agrego la palabra {nueva}, el resultado es: {lista}")


# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

# num=int(input("Número de palabras:"))
# lista=[]
# for i in range(1,num+1):
#     lista.append(input("Palabra:"))
# print(f"La lista ingresada es: {lista}")
# reemplazo= input("Ingrese la palabra que quiere eliminar: ")
# lista.remove(reemplazo)
# print(f"Se elimino la palabra '{reemplazo}' y lista quedo así: {lista}")


# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

# num=int(input("Número de palabras:"))
# lista1=[]
# for i in range(1,num+1):
#     lista1.append(input("Palabra:"))
# print(f"La primer lista ingresada es: {lista1}")

# num=int(input("Número de palabras:"))
# lista2=[]
# for i in range(1,num+1):
#     lista2.append(input("Palabra:"))
# print(f"La segunda lista ingresada es: {lista2}")

# for i in lista1:
#         for x in lista2:
#             if i == x:
#                 lista1.remove(i)
# print(f"la primer lista quedo asi: {lista1}")
# print(f"la segunda lista quedo asi: {lista2}")



# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

num=int(input("Número de palabras:"))
lista=[]
for i in range(1,num+1):
    lista.append(input("Palabra:"))
    lista2 = lista[::-1]

print(f"La primer lista quedo asi: {lista}")
print(f"La segunda lista quedo asi: {lista2}")