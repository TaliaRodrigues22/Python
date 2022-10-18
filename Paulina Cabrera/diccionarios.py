# #Practica de diccionarios


# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# direccion= input("Ingrese su direccion: ")
# telefono = int(input("Ingrese su numero telefonico: "))

# persona = {"Nombre": nombre, "Edad": edad, "Dirección": direccion, "Telefono": telefono}

# print(f"Tu nombre es {nombre} tienes {edad} años, vives en {direccion} y tu numero de telefono es {telefono} ")



# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# frutitas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

# fruta =input("Ingrese la fruta que esta buscando [le pedimos que ingrese la primer letra en mayuscula]: ")
# cantidad = int(input("Ingrese la cantidad que desea comprar: "))

# if fruta in frutitas:
#     print(f"El precio final por {cantidad}kg de {fruta} es igual a ${frutitas[fruta] * cantidad}")
# else:
#     print(f"Lo sentimos la fruta {fruta} no tiene stock")


# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# mes = {1:"enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre" }

# fecha = input("Introduzca una fecha con el siguiente formato: [dd/mm/aaaa] ")
# fecha = fecha.split("/") #permite usar / en el imput

# print(fecha[0], 'de', mes[int(fecha[1])], 'del', fecha[2])

# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# diccionario = {}

# nombre = input("Ingrese su nombre: ")
# diccionario.update({"Nombre": nombre})
# print(diccionario)

# edad = int(input("Ingrese su edad: "))
# diccionario.update({"Edad": edad})
# print(diccionario)

# genero = input("Ingrese el genero con que se identifica: ")
# diccionario.update({"Genero": genero})
# print(diccionario)

# telefono = int(input("Ingrese su numero telefonico: "))
# diccionario.update({"Número telefonico": telefono})
# print(diccionario)

# correo = input("Ingrese su correo electronico: ")
# diccionario.update({"Correo electronico": correo})
# print(diccionario)



# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas= {"2212": 15, "8040": 200, "3320": 100, "8415": 1500, "2020": 740}
usuario = input("¿Quieres añadir una nueva factura [escriba NF], pagar una factura existente [escriba FE] o terminar[S]: ")
usuario = usuario.swapcase()
if  (usuario == "NF"):
    numerofac= input("Ingrese el numero de factura:")
    importe = int(input("Ingrese el importe a abonar: "))
    facturas.update({numerofac: importe})    
    print(facturas)
elif (usuario == "FE"):
    print(facturas)
    numerofac= input("Ingrese el numero de factura:")
    print(f"Perfecto la factura: {numerofac} sera marcada como abonada")
    facturas.pop(numerofac)
    print(facturas)
else:
    print("hasta luego")
# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

# agenda = {"susana":1141590900, "berta":1120120, "manolo": 111456987, "jose":114568}

# quequiere = input("Hola bienvenidx a la agenda magica, que quieres hacer hoy? [A]-Añadir/modificar [B]-Buscar [C]-Borrar [D]-Listar")

# quequiere = quequiere.swapcase()

# if(quequiere == "A"):
#     nombre= input("Ingrese el nombre: ")
#     if nombre in agenda:
#         print(f"El numero de {nombre} es {agenda[nombre]}")
#         modif= input("Quieres modificarlo? [s] o [n]")
#         if modif == "s":
#             num= int(input("Ingrese el nuevo numero de telefono: "))
#             agenda[nombre] = num
#             print(agenda)
#     else:
#         telefono= int(input("Ingrese el numero de telefono"))
#         agenda.update({nombre:telefono})
#         print(agenda)
# elif(quequiere == "B"):
#     nombre= input("Ingrese el nombre: ")
#     e = agenda.get(nombre, "No tienes ese nombre en tu agenda")
#     print(e)
# elif(quequiere=="C"):
#     nombre= input("Ingrese el nombre: ")
#     if nombre in agenda:
#         print(f"Se eliminara a {nombre} de la agenda {agenda}")
#         agenda.pop(nombre)
#         print(agenda)
# elif (quequiere == "D"):
#     print(f"Su agenda actual es: {agenda.items()}")
# else:
#     print("opcion invalida ejecute el codigo nuevamente")
    
