# 1 Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y 
# luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

# num = int(input("Escriba un numero: "))
# can = input("Escriba la cantidad de palabras segun el numero ingresado: ")
# l1 = [can]
# print(l1)



# 2 Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas 
# veces aparece esa palabra en la lista.

# lista = input("Ingrese una lista: ")
# l1 = [lista]
# print(l1)
# palaPed = input("Ingrese una palabra de la lista: ")
# l1 = lista.count(palaPed)
# print(l1)    



# 3 Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la 
# primera por la segunda en la lista.

#CON LISTA YA CREADA
# lista1 = input("Ingrese una lista: ")    #debo crear una variable donde usar el append
# l1 = [lista1]
# print(l1)
# lista2 = input("Ingrese dos palabras: ")
# lista1[1] = [lista2]
# print(lista1)


# lista1 = ["manzana", "pera", "frutilla"]
# print(lista1)
# lista2 = input("Ingrese dos palabras: ")
# l1= lista1.insert(0, lista2)
# print(lista1)



# 4 Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa 
# palabra de la lista.

#CON LISTA YA CREADA
# preg = ["manzana", "pera", "banana", "ciruela", "uva", "cereza"]
# print(preg)
# preg2 = input("Ingrese una palabra de la lista para eliminar: ")
# lista = preg.remove(preg2)
# print(lista)


# preg = input("Ingrese una lista: ")
# l1 = [preg]
# print(l1)
# preg2 = input("Ingrese una palabra de la lista para eliminar: ")
# for i in l1:
#     l2 = preg.remove(len(str(preg2)))
#     print(preg)



# 5 Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera 
# lista los nombres de la segunda lista.

#CON LISTA YA CREADA
lis1 = ["manzana", "pera", "uva", "cereza", "ciruela", "banana"]
print(lis1)
lis2 = input("Ingrese las palabras a eliminar en la lista 1: ")
l3 = lis1.remove(lis2)
print(lis1)

# lis1 = input("Ingrese una lista: ")
# l1 = [lis1]
# print(l1)
# lis2 = input("Ingrese las palabras a eliminar en la lista 1: ")
# l2 = lis1.remove(lis2)
# print(l2)



# 6 Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual 
# a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
