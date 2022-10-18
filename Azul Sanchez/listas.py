#1 - Escriba un programa que permita crear una lista de palabras. 
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
# Por último, el programa tiene que escribir la lista.


numero=int(input("Ingrese número de palabras:"))
lista=["sol", "lluvia", "nubes", "pajaros"]
for i in range(1,numero+1):
    lista.append(input("Ingrese palabras:"))
print(lista)



#2. - Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

palabra=input("Ingrese una palabra:")
lista=["sol", "lluvia", "nubes", "pajaros"]

for i in lista:
    lista= lista.count(palabra)
print(lista)

#3- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida dos palabras y sustituya la primera por la segunda en la lista.

lista= ["gato", "perro", "mono"]
i=0
print("Lista: ",lista)
while i<0:    
    lista.append(palabra)
    i+=1 
palabra1= input("Ingrese una palabra de la lista: ")
palabra2= input("Ingrese una palabra para sustituirla: ")
    
indice= lista.index(palabra1)
lista.insert(indice, palabra2)
lista.remove(palabra1)
print(lista) 




#4- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y elimine esa palabra de la lista.

lista= ["mouse", "teclado", "parlantes", "auriculares"]
print("Lista", lista)

palabra= input("Ingrese una palabra: ")
lista.remove(palabra)
print(lista)

#5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
# elimine de la primera lista los nombres de la segunda lista.

lista1= ["mouse", "teclado", "parlantes", "auriculares"]
lista2= ["rosa", "tele", "celular", "mouse"]

eliminados=[]
for i in lista1:
    if i in lista2:
        lista1.remove(i)
        eliminados.append(i)
print("Primera lista", lista1)
print("Segunda lista", lista2)
print("Palabra eliminada", eliminados)

#6- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, pero al revés 
# (no se trata de escribir la lista al revés, sino de crear una lista distinta).

lista= ["mouse", "teclado", "parlantes", "auriculares"]

listaCopy=lista.copy()
print(listaCopy)
lista.reverse()
print(lista)
