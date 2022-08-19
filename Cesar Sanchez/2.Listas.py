# Listas 

# 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.


""" pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print (lista) """



# otra forma similar 

""" pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str (input("Escriba una palabra : "))

    lista.append(palabra)

    listaCreada = lista 

print (listaCreada)  """




# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.



""" pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print (lista)


palabraRepetida = str (input("Escriba una palabra para ver cuantas veces se repite: "))

repetidas = lista.count(palabraRepetida)

print ("La palabra ", palabraRepetida, " se repite :", repetidas) """





# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

""" pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print ("Las palabras de mi lista son: ", lista)


palabraASustituir = str (input ("Ingrese una palabra de la lista que desea sustituir: "))

palabraSustituta = str ( input ("Ingrese la palabra que sustituirá: "))

posicion = lista.index(palabraASustituir)  # Ubico la posción en la lista de la palabra que voy a sustituir 

# Una vez ubica la posición lo sustituyo 

lista.insert (posicion, palabraSustituta)            # Con la posición y la palabra que sustituirá lo ubico y lo reemplazo

print (lista)            # Imprimo y me sale en la posición la nueva palabra

lista.remove(palabraASustituir)    # Ahora elimino la palabra que he sustituido

print(lista) """



    


# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.


""" pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print (lista)

pedirPalabra = str ( input ("Escriba la palabra de la lista que desea eliminar: "))

lista.remove(pedirPalabra)

print (lista) """



# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

""" # Creo la primera lista

pedirNumero = int (input ("Escriba un número: "))

lista = []

for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print ("Los elementos de mi lista son ", lista)


# Creo otra lista 

numero2 = pedirNumero

lista2 = []

for i in range (numero2): 

    palabra2 = str(input("Escriba una palabra para la lista 2 : "))

    lista2.append(palabra2)

print ("Los elementos de mi lista 2 son: ", lista2)



listaEliminados = []                  # Creo una lista para agregar las palabras que eliminaremos

for i in lista :          # Recorro los elementos de la lista 

    if i in lista2 :           # Si los elementos estan en la lista2

        lista. remove(i)            # Elimino los repetidos de mi lista 2 en mi lista 1

        listaEliminados.append(i)             # Agrego en mi listaEliminados las palabras eliminadas 

print("mi lista queda: ",lista)

print ("Los elementos eliminados de mi lista son: ", listaEliminados)                 # Imprimo la lista cobn las palabras eliminadas  """




# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).


""" pedirNumero = int (input ("Escriba un número: "))

lista = []


for i in range (pedirNumero): 

    palabra = str(input("Escriba una palabra : "))

    lista.append(palabra)

print (lista)

cantidad = len(lista)

print(cantidad)

listaNueva = []

while cantidad > 0 :

    listaNueva.append(lista[cantidad - 1])

    cantidad -= 1

print(listaNueva) """


