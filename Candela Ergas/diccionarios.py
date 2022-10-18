# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre=input("Ingresá tu nombre: ")
edad=input("Ingresá tu edad: ")
direccion=input("Ingresá tu direccion: ")
telefono=input("Ingresá tu teléfono: ")

datos={"nombre":nombre, "edad":edad, "dirección":direccion, "teléfono":telefono}

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['dirección']} y su número de teléfono es {datos['teléfono']}")

# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70
precios={"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta=input("Ingresá que fruta querés: ")
kilos=int(input("Cuantos kilos querés?: "))


if fruta.capitalize() in precios:
    precio=precios[fruta.capitalize()]*kilos
    print(f"Llevar {kilos} de {fruta} cuesta ${round(precio,2)}")
else:
    print(f"No tenemos esa fruta,disculpá!")


# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}

fecha=input("Ingresá una fecha en formato dd/mm/aaaa : ")
fecha=fecha.split("/")

print(f"La fecha ingresada es {fecha[0]} de {meses[fecha[1]]} de {fecha[2]} ")
# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
datos={}
nombre=input("Ingresá tu nombre: ")
datos.update({"Nombre":nombre})
print(datos)

edad=input("Ingresá tu edad: ")
datos.update({"Edad:":edad})
print(datos)

sexo=input("Ingresá tu sexo biológico: ")
datos.update({"Sexo":sexo})
print(datos)

telefono=input("Ingresá tu telefóno: ")
datos.update({"Teléfono:":telefono})
print(datos)

correo=input("Ingresá tu correo electrónico: ")
datos.update({"Correo electrónico":correo})
print(datos)

# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
opcion=int(input("Que desea hacer? \n[1] Añadir una factura \n[2] Pagar una factura \n[3] Salir \n Ingrese la opción correspondiente: "))
aPagar={}
total=0
pagado=0
while opcion!=3:
    if opcion==1:
        nro=int(input("Ingrese el nro de factura: "))
        coste=float(input("Ingrese el coste de la factura: "))
        aPagar.update({nro:coste})
        total+=coste
        print(f"Hasta el momento se cobró ${pagado} y queda pendiente de cobro ${total}")
        print(aPagar)
    if opcion==2:
        factura=int(input("Ingresá el nro de factura a pagar: "))
        pago=aPagar.pop(factura)
        pagado+=pago
        total-=pago
        print(f"Hasta el momento se cobró ${pagado} y queda pendiente de cobro ${total}")
        print(aPagar)
    opcion=int(input("Que desea hacer? \n[1] Añadir una factura \n[2] Pagar una factura \n[3] Salir \n Ingrese la opción correspondiente: "))
print("Usted ha finalizado")
# if opcion!=1 and opcion!=2:
#     print("opción incorrecta!")
#     opcion=int(input("Que desea hacer? \n[1] Añadir una factura \n[2] Pagar una factura \n[3] Salir \n Ingrese la opción correspondiente: "))
        
# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

agenda={"Uno":1111,"Dos":2222,"Tres":3333,"TresB":3331}
opcion=int(input("Menú: \n[1]Añadir/modificar \n[2]Buscar \n[3]Borrar \n[4]Listar\nIngresá la opción: "))

if opcion==1:
    nombre=input("Ingresá un nombre: ").capitalize()
    if nombre in agenda:
        print(f"El número agendado para {nombre} es {agenda[nombre]}")
        mod=input("Deseas modificarlo? {si/no] : ")
        if mod=="si":
            nnum=int(input("Ingresá el nuevo número: "))
            agenda.update({nombre:nnum})
            print(f"El nuevo número de {nombre} es {agenda[nombre]}")
    else: 
        print(f"{nombre} no está agendado")
        nuevo=int(input("Ingresá su numero para guardarlo: "))
        agenda.update({nombre:nuevo})
        print(f"Perfecto!El número agendado para {nombre} es {agenda[nombre]}")
        
if opcion==2:
    nombre=input("Ingresá el nombre que buscas: ").capitalize()
    for i in agenda:
        if i.startswith(nombre):
            print(f"El número de {i} es: {agenda[i]}")

if opcion==3:
    nombre=input("Ingresá el nombre del contacto que queres eliminar: ").capitalize()
    if nombre in agenda:
        borrar=input("Confirmá la eliminación del contacto [si/no]: ")
        if borrar=="si":
            agenda.pop(nombre)
            print("Listo!Contacto eliminado")
        else:
            print("Ok,no lo borramos")
    else:
        print("Ese nombre no estaba agendado")

if opcion==4:
    print("Tus contactos agendados son: ")
    for nombre,num in agenda.items():
        print(f"{nombre}:{num}")
