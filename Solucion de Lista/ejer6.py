#Para crear la lista inversa, este programa puede incluir un bucle que recorra la lista una vez creada.
#Puesto que no se van a modificar los valores de la lista, la lista se puede recorrer directamente (for i in lista).
#En cada iteración del bucle, se añade el elemento de la lista inicial al principio de la lista inversa


def main():
  numero = int(input("Dígame cuántas palabras tiene la lista: "))

  if numero < 1:
      print("¡Imposible!")
  else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")

      inversa = []
      for i in lista:
          inversa = [i] + inversa
      print(f"La lista inversa es: {inversa}")


if __name__ == "__main__":
  main()