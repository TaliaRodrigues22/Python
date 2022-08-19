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

      eliminar = input("Palabra a eliminar: ")
      for i in range(len(lista) - 1, -1, -1):
          if lista[i] == eliminar:
              del lista[i]
      print(f"La lista es ahora: {lista}")


if __name__ == "__main__":
  main()