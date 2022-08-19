# 1 - Escriba un programa que permita crear una lista de palabras. 
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
# Por último, el programa tiene que escribir la lista.

cantidad = int(input("Cantidad de palabras: "))
palabras = []
for i in range(cantidad):
    palabras.append(input("Palabra: "))
print(palabras)

# 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

palabras = ['perro', 'pepe', 'gato', 'messi', 'agua', 'perro', 'perro']
palabraUsr = input('Palabra: ')

contador = palabras.count(palabraUsr)
print(f'Cantidad de apariciones de "{palabraUsr}": {contador}')

# 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida dos palabras y sustituya la primera por la segunda en la lista.

palabras = ['perro', 'pepe', 'gato', 'mesa', 'agua', 'hola', 'chao']
original = input('Palabra a cambiar: ')
sustituta = input('Por la palabra: ')
print(f'Lista antes del cambio: {palabras}')
indice = palabras.index(original)
palabras[indice] = sustituta
print(f'Lista después del cambio: {palabras}')

# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y elimine esa palabra de la lista.

palabras = ['perro', 'pepe', 'gato', 'mesa', 'agua', 'hola', 'chao']
palabraEliminar = input('Palabra a eliminar: ')
print(f'Lista antes del cambio: {palabras}')
indice = palabras.remove(palabraEliminar)
print(f'Lista después del cambio: {palabras}')

# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
# elimine de la primera lista los nombres de la segunda lista.

nombres1 = ['cami', 'pepe', 'gato', 'mesa', 'agua', 'hola', 'chao'] 
eliminadas = []
print(nombres1)
while True:
    palabraUsr = input("Ingresa una palabra a eliminar [para salir ingresa 0]: ")
    if(palabraUsr == '0'):
        break
    if palabraUsr in nombres1:
        eliminadas.append(palabraUsr)

for i in eliminadas:
    if i in nombres1:
        nombres1.remove(i)
        
print(f'Lista de eliminadas: {eliminadas}')
print(f'Lista original después del cambio: {nombres1}')

# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, 
# pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

lista1 = ['perro', 'pepe', 'gato', 'mesa', 'agua', 'hola', 'chao']
lista2 = []
for i in range(len(lista1)-1, -1, -1):
    lista2.append(lista1[i])
print(lista1)
print(lista2)