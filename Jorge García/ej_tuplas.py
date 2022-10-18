# 1-Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
# en dos listas y muestre por pantalla su producto escalar.

vector1 = (1,2,3)
vector2 = (-1,0,2) 

producto_escalar = 0

for i in range(len(vector1)):
    producto = vector1[i] * vector2[i]
    producto_escalar += producto
    
print(f'El producto escalar es = {producto_escalar}')

# # 2-Escribir un programa que almacene en una lista los 
# # siguientes precios: 50, 75, 46, 22, 80, 65, 8 
# # y muestre por pantalla el menor y el mayor de los precios.

precios = 50, 75, 46, 22, 80, 65, 8
print(f'Mínimo: {min(precios)}')
print(f'Máximo: {max(precios)}')

# 3-Escribir un programa que pregunte por una muestra de números, 
# separados por comas, los guarde en una lista y 
# muestre por pantalla su media y desviación típica.

numerosStr = input("Ingresa números separados por comas: ")
numeros = numerosStr.split(",")
print(numeros)
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
    
media = sum(numeros)/len(numeros)
sumaDesvios = 0
for i in numeros:
    desvio = pow(i - media, 2)
    sumaDesvios += desvio
varianza = sumaDesvios/len(numeros)
desviacion = varianza ** 0.5

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")