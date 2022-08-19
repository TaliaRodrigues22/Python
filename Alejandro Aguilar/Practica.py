# # <!-- Listas 

# # 1 - Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número
# # y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.


# def listita():
#   numero = int(input("Escriba cuantas palabras tiene la lista " ))
  
#   if numero < 1:
#       print("Error!")
#   else:
#       lista = []
#       for i in range(numero):
#           palabra = input(f"Escriba la palabra {i + 1}: ")
#           lista += [palabra]
#       print(f"La lista creada es: {lista}")

# listita()



# # 2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra
# # y diga cuántas veces aparece esa palabra en la lista.


# # 3- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras
# # y sustituya la primera por la segunda en la lista.

# def listaPalabras():
#   number = int(input("Indique cuantas palabras tiene la lista : "))
  
#   if number < 1:
#       print("Error!")
#   else:
#       lista = []
#       for i in range(number):
#           palabra = input(f"Escriba la palabra {i + 1}: ")
#           lista += [palabra]
#       print(f"La lista es: {lista} ")
      
#       bus = input("Reemplazar la palabra: ")
#       reem = input("Por la palabra: ")
#       for i in range(len(lista)):
#           if lista [i] == bus:
#               lista[i]  = reem
#       print(f"La lista actualizada es: {lista}")
      
# listaPalabras()
    



# 4- Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine
# esa palabra de la lista.

# lista = ["mouse", "teclado", "parlantes"]
# print(lista)
# palabra = input("Ingresa una palabra")

# lista.remove(palabra) 
# print(lista)




# 5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera
# lista los nombres de la segunda lista.


# lista = ["triangulo", "cuadrado", "rectangulo"]
# listaDos = ["estructura", "relieve", "tornado"]
# print(lista,listaDos)

# lista.remove

# listita=["mouse", "serpiente", "teclado", "silla", "marcador"]
# liston=[]
# for i in listita:
#     if i in listita:
#         listita.remove(i)
#         liston.append(i)               
# print(f"Primer lista: {listita}")
# print(f"La palabra '{i}' fue eliminado y se agrego a la segunda lista, {liston}")

# 6- Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
# igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta). -->

palabraDos = ["clima","mañana","tarde"]
palabraUno = []
palabraDos.reverse()
print(palabraDos)