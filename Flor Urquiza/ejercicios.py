#1 - Escriba un programa que permita crear una lista de palabras.
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de
# palabras para crear la lista. Por último, el programa tiene que escribir la lista.

num=int(input("Número de palabras:"))
lista=[]
for i in range(1,num+1):
     lista.append(input("Palabra:"))
		
print(lista)


#2 - Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

listaPalabras= [amor, perro, gato, gato, pez, agua]
print (listaPalabras)
palabra= input("Escriba una palabra: ")
for i in lista :
     lista= listaPalabras.count(palabra)
print (lista)


#3- Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

listaPalabras= ["mesa", "mantel", "perro", "gato", "lampara", "lluvia"]

primerPalabra= input("Ingrese una palabra: ")
segundaPalabra= input("Ingrese otra palabra: ")

listaPalabras [1] = primerPalabra
listaPalabras [2] = segundaPalabra
print (listaPalabras)

#4- Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y elimine esa palabra de la lista.

lista= ["perro", "carpa", "mano", "agua", "gato"]
print (lista)

palabraEliminada = input(("Ingrese una palabra de la lista para eliminar: "))

lista.remove(palabraEliminada)

print (lista)


#5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
# elimine de la primera lista los nombres de la segunda lista.


lista1=int(input("Cuantas palabras quiere escribir para la lista: "))
lista=[]
for i in range(1,lista1+1):
    palabra=input("palabra: ")
    lista.append(palabra)
print(lista)
X=0
eliminados=[]
while X <2:
    X+=1
    canteliminar = input("Elimine dos palabras: ")
    palabra2 = lista.remove(canteliminar)
    eliminados.append(canteliminar)
    print("eliminados:",eliminados)
    print("la lista quedo asi: ",lista)
    
    
#6- Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, cree una segunda lista igual a la primera, pero al revés 
# (no se trata de escribir la lista al revés, sino de crear una lista distinta)

lista= ["perro", "gato", "mono", "jirafa"]
lista2= lista*2
lista2.reverse()
print (lista2)
    



     
     
     

    