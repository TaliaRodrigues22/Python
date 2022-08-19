# # Practica de tuplas 
# *Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
import numpy as np
u=np.array([1,2,3])
v=np.array([-1,0,2])
pv=u.dot(v)
print("El producto escalar es: ",pv)

# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios=[50,75,46,22,80,65,8]
maximo=max(precios)
minimo=min(precios)
print("El maximo es: ", maximo, " y el minimo es: ", minimo)

# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

cant=int(input("Ingrese la cantidad de numeros: "))     #cantidad de numeros

array=[]
for i in range(cant):                                 #lista de numeros
    num=int(input("Ingrese cada uno de ellos: "))
    array.append(num)

suma=sum(array)
media=suma/cant                                        #promedio

numerador=0
for i in array:
    numerador+=(i-media)**2                            #varianza
varianzaMuestra=numerador/(cant-1)

desviacionTipica=varianzaMuestra**(0.5)         #desviacion tipica

print("La media es: ", media," y la desviacion tipica: ", desviacionTipica)