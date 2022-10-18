# *Realizar los 3 ejercicios con tuplas

# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
vectorA=(1,2,3)
vectorB=(-1,0,2)

producto=0
for i in vectorA:
    producto+= i*vectorB[vectorA.index(i)]
print("El producto escalar es: ",producto)

# 2-Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios=(50, 75, 46, 22, 80, 65, 8)
print("El mínimo es: ",min(precios)," y el máximo es: ",max(precios))

# 3-Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

nros=(input("Ingresá una lista de números separados por ',' :"))
lista=nros.split(",")

cant=len(lista)

#Pasa los nros de la lista a type int
for n in range(cant):
    lista[n]=int(lista[n]) 

total=sum(lista)
promedio= (total/cant) 

#Calculo varianza para poder calcular la desviacion típica
totalV=0
for n in lista:
    totalV+=(n-promedio)**2
varianza= totalV/cant 

desvT=(varianza**(0.5))

print(f"La lista ingresada es: {lista}, su media es: {round(promedio,2)} y su desviacion típica es: {desvT}")