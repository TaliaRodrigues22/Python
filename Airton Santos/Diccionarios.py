# #Practica de diccionarios

# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# def infoUsuario():

#     nombre = input("Ingrese su nombre")
#     direccion = input("Ingrese su direccion")
#     edad = input("Ingrese su edad")
#     telefono = input("Ingrese su teléfono")

#     dic1 = {}
#     dic1.update({"Nombre": nombre, "Edad" : edad, "Direccion" : direccion, "Telefono" : telefono})

#     print(f"{nombre} tiene {edad} años, vive en {direccion} y su numero de telefono es {telefono}")

# infoUsuario()


# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de 
# kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar 
# un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70


# def preciosFrutas():

#     frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera" : 0.85, "Naranja":0.70 }

#     fruta = input("Ingrese que fruta quiere comprar")
#     cantidad = int(input("Ingrese cuantos kilos quiere comprar"))


#     if frutas.get(fruta) == None:
#         print("Error, no encontramos esa fruta")
#     else:
#         calculo = frutas[fruta] * cantidad
#         print(calculo)

# preciosFrutas()


# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> 
# de aaaa donde <mes> es el nombre del mes.

# meses = {"01" :"Enero", 
#         "02" :"Febrero",
#         "03" : "Marzo",
#         "04" : "Abril", 
#         "05" : "Mayo", 
#         "06" : "Junio",
#         "07" : "Julio",
#         "08" : "Agosto",
#         "09" : "Septiembre",
#         "10" : "Octubre",
#         "11" : "Noviembre",
#         "12" : "Diciembre",
        
# }

# def preguntarFecha():

#     fecha = input("Ingrese una fecha en formato dd/mm/aaaa")
#     mes = fecha[3] + fecha[4]
#     mesMostrado = meses.get(mes)

#     print(fecha[:2], "de", mesMostrado, fecha[-4:])

# preguntarFecha()



# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# def infoPersonal():

#     dic = {}
    
#     nombre = input("Ingrese su nombre")
#     dic.update({"Nombre": nombre})
#     print(dic)
    
#     direccion = input("Ingrese su direccion")
#     dic.update({"Direccion": direccion})
#     print(dic)

#     celular = input("Ingrese su celular")
#     dic.update({"Celular": celular})
#     print(dic)


# infoPersonal()


# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de 
# factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará 
# del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad
#  pendiente de cobro.

# def facturas():

#     factura = {315 : 300 , 411 : 400}
#     cantidadPendiente = 0 
#     pagado = 0 

#     while True:


#         print("Qué operación desea realizar? Teclee:")
#         valor = int(input("1. Ingresar nueva factura / 2. Pagar factura / 3.Terminar de operar"))
#         total = 0 
        
#         if valor == 1:

#             nFactura = int(input("Ingrese el numero de factura"))
#             costeFactura = int(input("Ingrese el coste de la factura"))
#             factura.update({nFactura : costeFactura})
#             cantidadPendiente = sum(factura.values())
#             print(f"La cantidad abonada es de {pagado}")
#             print(f"La cantidad a pagar es {cantidadPendiente}")

#         elif valor == 2:    

#             nroFactura = int(input("Ingrese el numero de factura que desea pagar"))
#             pagado = sum(factura.pop(nroFactura))
#             cantidadPendiente = factura.values()
#             print(f"La cantidad abonada es de {pagado}")
#             print(f"La cantidad a pagar es {cantidadPendiente}")

#         elif valor == 3:

#             print("Saliendo del sistema...")
#             break


# facturas()



# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

