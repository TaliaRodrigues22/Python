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

      numero2 = int(
          input("Dígame cuántas palabras tiene la lista de palabras a eliminar: ")
      )

      if numero2 < 1:
          print("¡Imposible!")
      else:
          eliminar = []
          for i in range(numero2):
              palabra = input(f"Dígame la palabra {i + 1}: ")
              eliminar += [palabra]
          print(f"La lista de palabras a eliminar es: {eliminar}")

          for i in eliminar:
              for j in range(len(lista) - 1, -1, -1):
                  if lista[j] == i:
                      del lista[j]
          print(f"La lista es ahora: {lista}")


if __name__ == "__main__":
  main()