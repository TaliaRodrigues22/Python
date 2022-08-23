#Practica de diccionarios


# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono 
# es <teléfono>.

# name= input("Ingrese su nombre: ")
# age= int(input("Ingrese la edad: "))
# direction: input("Ingrese su direccion: ")
# phone: int(input("Ingrese un numero de telefono: "))
# dic={"Nombre":name,"Edad":age,"Direccion":direction,"Telefono":phone}
# print(name["Nombre"], " tiene ", age["Edad"] ," años, vive en ", direction["Direccion"] ," y su número de teléfono es ", phone["Telefono"])


# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato
# dd de <mes> de aaaa donde <mes> es el nombre del mes.



# dias = input("Ingresa un dia: ")
# mes = input("Ingresa un mes: ")
# año = input("Ingresa un año: ")

# meses = {"1": "Enero",
#               "2" : "Febrero",
#               "3" : "Marzo",
#               "4" : "Abril",
#               "5" : "Mayo",
#               "6" : "Junio",
#               "7" : "Julio",
#               "8" : "Agosto",
#               "9" : "Septiembre",
#               "10": "Octubre",
#               "11": "Noviembre",
#               "12": "Diciembre "}
# # print (meses)
# print ("dia" , dias, "del mes ", meses[mes], "del año", año)




# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que
# se añada un nuevo dato debe imprimirse el contenido del diccionario.

# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se 
# almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el 
# coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar 
# una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se 
# añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del 
# diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y
# la cantidad pendiente de cobro.

# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono.
# El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el
# teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

