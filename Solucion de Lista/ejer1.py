
#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
#Este programa puede incluir un bucle que se ejecute tantas veces como palabras tiene la lista.
#En cada iteración del bucle, se pide un valor y se añade a la lista.
def main ():
  numero = int(input("Dígame cuántas palabras tiene la lista: "))

  if numero < 1:
      print("¡Imposible!")
  else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")


if __name__ == "__main__":
  main()