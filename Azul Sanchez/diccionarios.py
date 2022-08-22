#1.Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje tiene años, vive en <dirección> 
# y su número de teléfono es <teléfono>.

Nombre= str(input("Ingrese su nombre: "))
Edad= int(input("Ingrese su edad: "))
Dirección= str(input("Ingrese su dirección: "))
Teléfono= int(input("Ingrese su número telefónico: "))

dicc= {"nombre": Nombre, "edad": Edad, "dirección": Dirección, "teléfono": Teléfono}

print(dicc["nombre"], "tiene", dicc["edad"], "años", "vive en", dicc["dirección"], "y su número de teléfono es:", dicc["teléfono"])

#2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y 
# muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#tabla: Fruta Precio Plátano 1.35 Manzana 0.80 Pera 0.85 Naranja 0.70

venta = {"plátano":1.35, "manzana":0.8, "pera":0.85, "naranja":0.7}
fruta = input("¿Qué fruta quiere llevar? ")
kg = float(input("Cuántos kilos? "))
if (fruta in venta):
    print(kg, "kilos de", fruta, "salen: ",venta[fruta]*kg)
else: 
    print("La fruta", fruta, "no está disponible")


#3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses= {"01":"enero", "02":"febrero","03":"marzo", "04": "abril", "05":"mayo","06": "junio","07": "julio", "08": "agosto", "09": "septiembre", "10": "octubre","11": "noviembre","12":"diciembre"}

dia= int(input("Ingrese el dia: "))
mes= (input("ingrese el mes: "))
año= int(input("ingrese el año: "))

print("La fecha es: ", dia ," de ", meses.get(mes), " del ", año )


#4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

dicc= {}

nombre= input("Ingrese su nombre: ")
dicc.update({"nombre":nombre})
print(dicc)

edad= int(input("Ingrese su edad: "))
dicc.update({"edad":edad})
print(dicc)
    
sexo= input("Ingrese su sexo: ")
dicc.update({"Sexo":sexo})
print(dicc)
          
teléfono= int(input("Ingrese su número telefónico: "))
dicc.update({"Teléfono":teléfono})
print(dicc)

#5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste 
# y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura 
# y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento 
# y la cantidad pendiente de cobro.

dicc= {}



#6-Escribir un programa que implemente una agenda. 
# En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:

#Añadir/modificar: Nos pide un nombre. 
# Si el nombre se encuentra en la agenda, debe mostrar el teléfono 
# y, opcionalmente, permitir modificarlo si no es correcto. 
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
# Buscar: Nos pide una cadena de caracteres, 
# y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena. 
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda. 
# Listar: Nos muestra todos los contactos de la agenda. Implementar el programa con un diccionario.

agenda= {"lucia": 11405872, "alberto": 1152698453, "susana": 1195623487, "maria": 1135498762}
opcion= input("Elige una opcion: 1. Añadir/modificar 2. Buscar 3. Borrar 4. Listar 5. Salir")


if opcion == "1":
    nombre = input("Nombre del contacto:") 
        
    if nombre in agenda:
        print(f"El numero de {nombre} es {agenda[nombre]}")
    modificar= input("¿Deseas modificarlo? [si] o [no]")
        if modificar == "si":
            numero= int(input("Ingrese el nuevo numero de telefono: "))
            agenda[nombre] = numero
            print(agenda)
    else:
        telefono= int(input("Ingrese el numero de telefono"))
        agenda.update({nombre:telefono})                             
        print(agenda)
    
elif opcion == "2":                                                        #revisar
    nombre= input("Ingrese el nombre: ")    
    print(agenda.get(nombre, "No tienes ese nombre en tu agenda"))

elif opcion == "3":
    nombre= input("Ingrese el nombre: ")
    if nombre in agenda:
        print(f"Se eliminara a {nombre} de la agenda {agenda}")
        agenda.pop(nombre)
        print(agenda)

elif opcion == "4":
    for nombre, numero in agenda.items():
            print(nombre,"->",numero)
            
elif opcion == 5:
        break
    else:
        print("Opción incorrecta")


