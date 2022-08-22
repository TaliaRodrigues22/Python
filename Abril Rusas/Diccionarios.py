#Practica de diccionarios


# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
n=input("Ingrese su nombre: ")
e=int(input("Ingrese su edad: ")) 
d=input("Ingrese su direccion: ")
t=int(input("Ingrese su telefono: ")) 
dic={"Nombre":n,"Edad":e,"Direccion":d,"Telefono":t}
print(dic["Nombre"], " tiene ", dic["Edad"] ," años, vive en ", dic["Direccion"] ," y su número de teléfono es ", dic["Telefono"])

# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
precios={"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
fruta=input("Ingrese la fruta que desea comprar: ")
if fruta in precios:
    kg=int(input("Ingrese cuantos kg desea llevar: "))
    precio=precios[fruta]*kg
    print("En total serian $", precio)
else:
    print("Lo lamento, no tenemos esa fruta")

# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

dia=int(input("Ingrese el dia de la fecha :"))
mes=int(input("Ingrese el mes (numericamente): "))
año=int(input("Ingrese el año: "))

# print(dia, " de ", meses[mes-1], " del ", año )
# # 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
dicc={}

nombre=input("Ingrese su nombre: ")
dicc.update({"Nombre: ":nombre})
print(dicc)

edad=int(input("Ingrese su edad: "))
dicc.update({"Edad: ":edad})
print(dicc)

sexo=input("Ingrese su sexo biologico: ")
dicc.update({"Sexo: ":sexo})
print(dicc)

tel=int(input("Ingrese su telefono: "))
dicc.update({"Telefono: ":tel})
print(dicc)

# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
dic={}
opcion=int(input("[1] Desea añadir una factura \n[2] Desea pagar una factura \n[3] Salir \nMarque el numero de la operacion que desee ejecutar: "))
pagado=0
pendiente=0

while opcion!=3:
    if opcion==1:
        factura=int(input("Ingrese el numero de factura: "))
        coste=float(input("Ingrese el costo de la factura: "))
        dic.update({factura:coste})
        pendiente+=coste
        opcion=int(input("[1] Desea añadir una factura \n[2] Desea pagar una factura \n[3] Salir \nMarque el numero de la operacion que desee ejecutar: "))
    if opcion==2:
        factura=int(input("Ingrese el numero de factura: "))
        pagado+=dic.pop(factura)
        pendiente-=pagado
        opcion=int(input("[1] Desea añadir una factura \n[2] Desea pagar una factura \n[3] Salir \nMarque el numero de la operacion que desee ejecutar: "))

print("Usted ha finalizado")
print("Usted ha pagado: ", pagado, "\nUsted debe: ", pendiente)

# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.
agenda={"gachi":11111111,"pachi":22222222,"gabriel":33333333}
opcion=int(input("[1] Añadir/Modificar \n[2] Buscar \n[3] Borrar \n[4] Mostrar agenda \n[5] Salir \nMarque el numero de la operacion que desee ejecutar: "))

while opcion!=5:
    if opcion==1:
        contacto=input("Ingrese un contacto: ")
        if contacto in agenda:
            print("El numero de su contacto es: ", agenda[contacto])
            opcion=input("Desea modificarlo? [si/no]: ")
            if opcion =="si":
                numero=int(input("Ingrese el nuevo numero: "))
                agenda.update({contacto:numero})
                print("El numero ha sido modificado")
        else:
            numero=int(input("Ingrese el numero: "))
            agenda.update({contacto:numero})
            print("Se ha agregado un nuevo contacto a la agenda")
        opcion=int(input("[1] Añadir/Modificar \n[2] Buscar \n[3] Borrar \n[4] Mostrar agenda \n[5] Salir \nMarque el numero de la operacion que desee ejecutar: "))   

    if opcion==2:
        string=input("Ingrese el contacto que desea buscar: ")
        for contactos in agenda:
            if contactos.startswith(string)==True:
                print(contactos,":",agenda[contactos])
        opcion=int(input("[1] Añadir/Modificar \n[2] Buscar \n[3] Borrar \n[4] Mostrar agenda \n[5] Salir \nMarque el numero de la operacion que desee ejecutar: "))  

    if opcion==3:
        contacto=input("Ingrese el contacto que desea borrar: ")
        agenda.pop(contacto)
        print("El contacto ha sido borrado")
        opcion=int(input("[1] Añadir/Modificar \n[2] Buscar \n[3] Borrar \n[4] Mostrar agenda \n[5] Salir \nMarque el numero de la operacion que desee ejecutar: "))

    if opcion==4:
        print(agenda)
        opcion=int(input("[1] Añadir/Modificar \n[2] Buscar \n[3] Borrar \n[4] Mostrar agenda \n[5] Salir \nMarque el numero de la operacion que desee ejecutar: "))
