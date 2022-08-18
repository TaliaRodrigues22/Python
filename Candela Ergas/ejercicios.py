#1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

cant=int(input("Ingresá(con números) la cantidad de palabras: "))
lista=[]
while len(lista)<cant :
    palabra=input("Ingresá una palabra: ")
    lista.append(palabra)
print("La lista de palabras es: ",lista)

#2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

listaNueva=[]
palabras=input("Ingresá, de a una, las palabras para la lista. Cuando termines escribí 'listo' ")
while palabras!="listo":
    listaNueva.append(palabras)
    palabras=input("Ingresá otra palabra: ")

sel=input("Ingresá una palabra y te diré cuantas veces aparece en la lista creada: ")
if listaNueva.count(sel)!=0 : 
    print("La palabra '",sel, "' aparece ",listaNueva.count(sel)," veces en la lista creada.")
else:
    print("La palabra '",sel,"'no está en la lista creada.")

#3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

listaNueva=[]
palabras=input("Ingresá, de a una, las palabras para la lista. Cuando termines escribí 'listo' ")
while palabras!="listo":
    listaNueva.append(palabras)
    palabras=input("Ingresá otra palabra: ")

print("La lista es la siguiente: ",listaNueva)
palA=input("Ingresá que palabra de la lista querés reemplazar: ")
palB=input("Ingresá por cuál la queres reemplazar: ")

if palA in listaNueva:
    listaNueva[listaNueva.index(palA)]=palB
    print("Hecho! Asi quedó la lista: ",listaNueva)
else:
    print("La palabra '",palA,"' no estaba en la lista")

#4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

listaNueva=[]
palabras=input("Ingresá, de a una, las palabras para la lista. Cuando termines escribí 'listo' ")
while palabras!="listo":
    listaNueva.append(palabras)
    palabras=input("Ingresá otra palabra: ")

print("La lista es la siguiente: ",listaNueva)
palA=input("Ingresá que palabra de la lista querés eliminar: ")

if palA in listaNueva:
    listaNueva.remove(palA)
    print("Hecho! Asi quedó la lista: ",listaNueva)
else:
    print("La palabra '",palA,"' no estaba en la lista")

#5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

listaNueva=[]
palabras=input("Ingresá, de a una, los nombres para la lista. Cuando termines escribí 'listo' ")
while palabras!="listo":
    listaNueva.append(palabras)
    palabras=input("Ingresá otra palabra: ")

listaBorrar=[]
nombres=input("Bien!Ahora ingresá, de a uno, los nombres que quisieras borrar. Cuando termines escribí 'listo' ")

while nombres!="listo":
    if nombres in listaNueva:
        listaBorrar.append(nombres)
        nombres=input("Perfecto! Ingresá otro nombre (o listo si deseas terminar): ")
    else:
        print("Ese nombre no se encuentra en la lista")
        nombres=input("Ingresá otro nombre: ")

for nombre in listaBorrar:
    listaNueva.remove(nombre)

print("Hecho!Asi quedó el listado de nombres: ",listaNueva)

#6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
listaNueva=[]
palabras=input("Ingresá, de a una, las palabras para la lista. Cuando termines escribí 'listo' ")
while palabras!="listo":
    listaNueva.append(palabras)
    palabras=input("Ingresá otra palabra: ")

listaB=[]
x=len(listaNueva)
while x>0:
    listaB.append(listaNueva[x-1])
    x-=1

print(listaNueva)
print(listaB)