# #Practica de diccionarios


# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# direccion = input("Ingrese su direccion: ")
# telefono = input("Ingrese su telefono: ")
# datos = {}
# datos.update({"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono})

# print("Hola {} tiene {} años, vive en {} y su número de teléfono es {}".format(datos["nombre"], datos["edad"], datos["direccion"], datos["telefono"]))



# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	   Precio
# Plátano	1.35
# Manzana	0.80
# Pera	    0.85
# Naranja	0.70

# frutas = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
# fruta = input("Que fruta desea comprar?: ")

# if fruta not in frutas:
#     print("Lamentablemente no tenemos esa fruta...")
# else: 
#     print("Si la tenemos...")
#     kilos = int(input("Cuantos kilos desea comprar?: "))
#     precio = frutas[fruta]
#     precioFinal = kilos * precio
#     print(f"El precio de la {fruta} por llevar {kilos}kg es: ${precioFinal}")


# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
# meses = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubbre", "11": "Noviembre", "12": "Diciembre"}
# fecha = input("Ingrese la fecha dd/mm/aaaa: ")
# listaFecha = fecha.split("/")
# dia = listaFecha[0]
# mes = listaFecha[1]
# año = listaFecha[2]
# for x in meses:
#     if x == mes:
#         print(f"{dia} de {meses[x]} de {año}!")


# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
# datos = {}
# print("Escriba 'exit' para terminar con la ejecución.")
# print("-" * 50)
# while True:
#     clave = input("Ingrese la clave del diccionario: ")
#     if clave == "exit":
#         print("El ciclo finalizó!")
#         break
#     if datos.get(clave) == None:
#         valor = input("Ingrese el valor: ")
#         datos.update({clave : valor}) 
#     else:
#         print("La clave ingresa ya está registrada!")
    
#     print("El diccioario es", datos)
#     print("_" * 50)



# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


# facturas = {}
# while True:
#     print("~" * 120)
#     operacion = input("¿Qué operacion desea realizar 1 (agregar factura), 2 (pagar factura), 3 (consultar facturas) y 4 (terminar operación): ")
#     if operacion == "1":
#         idFactura = input("Ingrese el numero de factura: ")
#         if facturas.get(idFactura) == None:
#             valorFactura = int(input("Ingrese el valor monetario: "))
#             facturas.update({idFactura : valorFactura}) 
#             print("Factura ingresada en sistema!")
#         else:
#             print("La factura ingresa ya está registrada!")
#     elif operacion == "2":
#         pagarFactura = input("Ingrese el número de factura: ") 
#         if facturas.get(pagarFactura) != None:
#             facturas.pop(pagarFactura)
#             print("Factura pagada!")
#         else:
#             print("La factura ingresa no está registrada!")
#     elif operacion == "3":
#         if len(facturas) == 0:
#             print("No tiene facturas pendientes!")
#         else:
#             suma = 0
#             print("Lista de facturas:")
#             for x in facturas:
#                 print(f"_Numero de factura: {x} y su coste: ${facturas[x]}")
#                 suma += facturas[x]
#             print("_" * 45)
#             print(f"El saldo total hasta el momento es: ${suma}")
#     elif operacion == "4":
#         print("Fin de operacion!")
#         break
#     else:
#         print("Esta operación no existe, vuelva a intentar")

    


# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.
validar = True
def exit(x):
    print("Fin de operacion!")
    x = False
    return x

agenda = {}
while validar:
    print("~" * 150)
    operacion = input("¿Qué operacion desea realizar 1 (Añadir/modificar contacto), 2(buscar contacto), 3(Borrar contacto), 4(Mostrar contactos) y 5(Terminar operacion): ")
    if operacion == "1":
        nombre = input("Ingrese un nombre: ")
        if agenda.get(nombre) == None:
            telefono = input("Ingrese el telefono de {}: ".format(nombre))
            agenda.update({nombre : telefono}) 
            print("Contacto ingresado a la agenda!")
        else:
            print(f"El telefono de {nombre} es: {telefono}")
            cambiarTel = input("Desea cambiar el numero de telefono de {}? (y/n): ".format(nombre))
            if cambiarTel == "y":
                telefono = input("Ingrese el nuevo telefono de {}: ".format(nombre))
                agenda.update({nombre : telefono})
                print("Contacto actualizado en la agenda!")

    elif operacion == "2":
        busqueda = input("Ingrese el nombre a busar: ")
        for x in agenda:
            if(x.startswith(busqueda)):
                print(f"_Nombre: {x} y su telefono: {agenda[x]}")

    elif operacion == "3":
        if len(agenda) == 0:
            print("No hay contactos para eliminar")
        else:
            eliminar = input("Ingrese el nombre del contacto a eliminar: ") 
            if agenda.get(eliminar) != None:
                agenda.pop(eliminar)
                print("Contacto eliminado!")
            else:
                print("El contacto ingresado no se encuentra")

    elif operacion == "4":
        if len(agenda) == 0:
            print("No tiene ningun contacto en la agenda!")
        else:
            print("Lista de contactos:")
            for x in agenda:
                print(f"_Nombre: {x} y su telefono: {agenda[x]}") 

    elif operacion == "5":
        exit(validar)

    else:
        print("Esta operación no existe, vuelva a intentar")    

