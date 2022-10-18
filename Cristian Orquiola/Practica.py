# Listas 

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

# num=int(input("cuantas palabras quiere escribir? ingrese un numero: "))
# lista=[]
# for i in range(1,num+1):
#     lista.append(input("Palabra: "))
# print(lista)

# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

# lista=["hola","como","estas","hola","hola","como","estas","hola","hola","como","estas","hola"]
# print(lista)
# x = input("que palabra de la lista quiere contar: ")
# for i in lista:
#     i = lista.count(x)
# print("aparece", i," veces en la lista")



# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

# palabra = ["hola","como","estas","todo","bien"]
# print(palabra)
# palabra1 = input("escriba una palabara nueva para sustituir a la segunda plabra de la lista: ")
# palabra2 = input("ingrese otra palabra :")

# palabra [1] = palabra1

# print(palabra)

# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

# lista=["hola","amigo","como","estas","chau"]
# print(lista)
# x=input("ingrese la palabra de la lista que quiera eliminar: ")
# lista.remove(x)
# print(lista)

# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.


# from re import X


# lista1=int(input("cuantas palabras quiere escribir para la lista: "))
# lista=[]
# for i in range(1,lista1+1):
#     palabra=input("palabra: ")
#     lista.append(palabra)
# print(lista)
# X=0
# eliminados=[]
# while X <2:
#     X+=1
#     canteliminar = input("elimine dos palabras: ")
#     palabra2 = lista.remove(canteliminar)
#     eliminados.append(canteliminar)
#     print("eliminados:",eliminados)
#     print("la lista quedo asi: ",lista)
 



# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

# lista3 = ["amigo","como","hola"]
# lista4 = lista3
# lista4.reverse()
# print(lista4)
