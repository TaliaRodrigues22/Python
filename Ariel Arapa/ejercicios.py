# Listas

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
num = int(input("Ingrese un numero: "))
lista1 = []
while 0 < num:
    print("Le quedan", num, "por escribir!")
    string = input("Ingrese una palabra para agregar a la lista: ")
    lista1.append(string)
    num -= 1

print("La lista es la siguiente:", lista1)


# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
lista2 = ["Cleo", "Aquiles", "gatitos", "escritorio", "celular", "gatitos"]
palabra = input("Ingrese una palabra: ")

if palabra not in lista2:
    print("La palabra ingresada no se encuentra en la lista")
else:
    cantidad = lista2.count(palabra)
    print("La palabra", palabra, "se repite", cantidad, "veces.")


# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
lista3 = ["Cleo", "Aquiles", "gatitos", "escritorio", "celular", "gatitos"]
pal1 = input("Ingrese la palabra para sustituir: ")

if pal1 in lista3:
    pal2 = input("Ingrese la nueva palabra: ")
    indice = lista3.index(pal1)
    lista3[indice] = pal2   
else: 
    print("La palabra", pal1, "no se encuentra en la lista")

print(lista3)

# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
lista4 = ["Cleo", "Aquiles", "gatitos", "escritorio", "celular", "gatitos"]
pal1 = input("Ingrese la palabra para eliminar: ")

if pal1 in lista4:
    print("La palabra", pal1, "se elimino de la lista")
    lista4.remove(pal1)
else:
    print("La palabra", pal1, "no se encuentra en la lista")

print(lista4)


# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
lista50 = ["Cleo", "Aquiles", "gatitos", "escritorio", "celular", "master"]
lista51 = ["escritorio", "celular", "gatitos"]

for x in lista51:
    if x in lista50:
        indice = lista50.index(x)
        lista50.pop(indice)

print(lista50)
print(lista51)


# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
lista60 = ["Cleo", "Aquiles", "gatitos", "escritorio", "celular", "master"]

lista61 = []
i = len(lista60)

while 0 < i:
    lista61.append(lista60[i - 1])
    i -= 1

print(lista61)