# Listas  
Una lista es una estructura de datos en la que puedes añadir elementos para su posterior uso. Como en otros lenguajes de programación, las listas permiten guardar cualquier tipo de dato, ya sea enteros, cadenas, objetos e incluso otras listas.
## Como trabajar con listas en Python 
Declarar lista

my_lista = []
My_Lista = list()

## Unir listas

my_lista =[1]
mylista2 =[2,3,4]
my_lista3 = my_lista + my_lista2
my_lista3 # [1,2,3,4]
 
 ## PArtir listas como slices

 my_lista = [1,2,3]
my_lista[1:] = [2,3]

## Extender una lista

my_lista = [1]
my_lista2 = [2,3,4]
my_lista.extend(my_lista2) # [1,2,3,4]
## Multiplicar listas

my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']

## eliminar el ultimo elemento de la lista 

my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]

## Ordenar lista

my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]

## Eliminar un elemento

my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

## Eliminar si conocemos su valor

my_lista = [1,2,3,4,5]
my_lista.remove(3)
my_lista #[1,2,4,5]

## Para saber que metodo hay dentro de un elemento

my_lista = [1,2,3,4,5]
dir(my_lista) # ['__add__', '__class__', '__contains__', ...

## Modificar un elemento 

my_lista = [1,2,3,4,5]
my_lista[0] = 100
my_lista # [100,2,3,4,5]

## Añadir un elemento al final
my_lista = [1,2,3,4,5]
my_lista.append(6)
my_lista # [1,2,3,4,5,6]

## Organizar una lista

my_lista = [2,5,1,3,4]
my_lista.sort() #[1,2,3,4,5]

# Métodos adicionales para listas

* .sorted()
También ordena como sort() pero modifica la lista inicial
* .clear()
Vacía la lista
*.count()
Cuenta las veces que esta un elemento en lista
*.index()
Indica la posición donde esta un elemento de la lista
*.insert()
Inserta un elemento en una posición dada ej: lista.insert(posición,item)
*.reverse()
Le da la vuelta a una lista

* Suma **(+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
 *Multiplicación **(*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]
Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]

* Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]
** Eliminar elemento **dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]
** Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]
** Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]
** Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]
** Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]

* Range creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
* Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5
