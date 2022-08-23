# Diccionarios (dict)

* Los diccionarios son estructuras que contienen una colección de elementos de la forma clave: valor separados por comas y encerrados entre llaves. Las claves deben ser objetos inmutables y los valores pueden ser de cualquier tipo. Necesariamente las claves deben ser únicas en cada diccionario, no así los valores.

* Vamos a definir un diccionario llamado edades en el cual cada clave será un nombre y el valor una edad:

edades = {"Ana": 25, "David": 18, "Lucas": 35, "Ximena": 30, "Ale": 20}

* Puede acceder a cada valor de un diccionario mediante su clave, por ejemplo, si quisieramos obtener la edad de la clave Lucas se tendría que escribir:

edades["Lucas"]

35


### Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

### Operaciones en diccionarios
* .keys():Retorna la clave de nuestro elemento.

* .values(): Retorna una lista de elementos (valores del diccionario).

* .items(): Devuelve lista de tuplas (primero la clave y luego el valor).

* .clear(): Elimina todos los items del diccionario.

* .pop(“n”): Elimina el elemento ingresado.

Cómo trabajar con diccionarios
Definir función principal

def run():
    # Defino el diccionario, agrego los valores.
    mi_diccionario = {
      'llave1' : 1,
      'llave2' : 2,
      'llave3' : 3,
    }


* Imprimir las llaves del diccionario utilizando un bucle for. Con ‘.keys()’ estamos llamando a imprimir las llaves, no los valores.

 for llave in mi_diccionario.keys():
        print(llave)

* Imprimir los valores del diccionario empleando un bucle for. Con ‘.values()’ estoy llamando a imprimir los valores.

 for valores in mi_diccionario.values():
        print(valores)

* Imprimir las llaves y los valores usando ‘.items()’. Para esto, coloco las variables llave e items.

for llave, items in mi_diccionario.items():
        print("La llave: '" + llave + "' contiene el item: " + str(items))

if __name__ == '__main__':
    run()