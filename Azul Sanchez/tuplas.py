#1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

lista1= (1,2,3)
lista2= (-1,0,2)
producto= 0
for i in range(len(lista1)):                     #range:Crea una lista inmutable de números enteros en sucesion aritmetica.
    producto= lista1[i] * lista2[i]              #len : para reccorer la lista
print("El producto escalar de", lista1, "y", lista2, "es: ", producto)                                    



#2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.

precios= (50, 75, 46, 22, 80, 65, 8,)

minimo= precios[0]
maximo= precios[0]

for precio in precios:
    if precio < minimo:
        min= precio
    elif precio > maximo:
        maximo= precio
print("El menor de los precios es: ", minimo)
print("El mayor de los precios es: ", maximo)


#3-Escribir un programa que pregunte por una muestra de números, separados por comas, 
# los guarde en una lista y muestre por pantalla su media y desviación típica.

cantidad=int(input("Ingrese la cantidad de numeros: "))     #cantidad de numeros

lista=[]
for i in range(cantidad):                                 #lista de numeros
    num=int(input("Ingrese cada uno de ellos: "))
    lista.append(num)

suma=sum(lista)
media=suma/cantidad                                        #promedio

numerador=0
for i in lista:
    numerador+=(i-media)**2                            #varianza
varianzaMuestra=numerador/(cantidad-1)

desviacionTipica=varianzaMuestra**(0.5)         #desviacion tipica

print("La media es: ", media," y la desviacion tipica: ", desviacionTipica)

