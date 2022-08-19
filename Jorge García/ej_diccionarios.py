# 1 - Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

persona = {
    'nombre': '',
    'edad': '',
    'direccion': '',
    'teléfono': ''
}

for clave in persona.keys():
    dato = input(f"Ingresa tu {clave}: ")
    persona[clave] = dato
    
print(f'{persona["nombre"]} tiene {persona["edad"]} años, vive en {persona["direccion"]} y su número de teléfono es {persona["teléfono"]}')

# 2-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

precios_frutas = {
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

frutaUsr = input("Ingresa la fruta: ").capitalize()
kilosUsr = float(input("Ingresa los kilos que quieres comprar: "))

precioPorKilo = precios_frutas.get(frutaUsr)
if(precioPorKilo != None):
    precioTotal = precioPorKilo * kilosUsr
    print(f"El precio total es de: {precioTotal}$")
else:
    print("La fruta ingresada no la vendemos.")

# 3-Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
# muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
    7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

fechaUsr = input("Fecha [dd/mm/aaaa]: ")
fechaSeparada = fechaUsr.split('/')

if(len(fechaSeparada) == 3 and int(fechaSeparada[0]) > 0 and int(fechaSeparada[0]) <= 31):
    mes = int(fechaSeparada[1])
    if(meses.get(mes) != None):
        print(f'{fechaSeparada[0]} de {meses[mes]} de {fechaSeparada[2]}') 
    else:
        print("¡Mes inválido!") 
else:
    print("Fecha inválida")

# 4-Escribir un programa que cree un diccionario vacío y lo vaya llenado 
# con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

respuesta = 2
persona = {}
while respuesta != 1:
    dato = input("Ingresa el dato que quieres agregar: ")
    valor = input(f"Ingresa tu {dato}: ")
    persona[dato] = valor
    print(persona)
    respuesta = int(input("Si quieres salir ingresa [1], si no ingresa [2]: "))

# 5-Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas = {
    1: 1000,
    2: 4500,
    3: 5500,
    4: 2400
}

opcion = 0
acumuladorCobro = 0
while opcion != '3':
    opcion = input("\n--- Opciones ---\n[1] Agregar factura \n[2] Pagar factura existente \n[3] Salir \n\nOpción: ")
    if(opcion == '1'):
        numeroFactura = int(input("Ingresa el número de la nueva factura: "))
        if(numeroFactura in facturas):
            print("\n¡Ya existe la factura!\n")
        else:
            costeFactura = float(input("Ingresa el coste de la factura: "))
            facturas[numeroFactura] = costeFactura
            print('\n¡Factura agregada exitosamente!\n')
    elif(opcion == '2'):
        print(f'Facturas -> {facturas}')
        numeroFactura = int(input("Ingresa el número de la factura a pagar: "))
        if(numeroFactura in facturas):
            facturaEliminada = facturas.pop(numeroFactura)
            acumuladorCobro += facturaEliminada
            print(f"\nSe pago la factura de: {facturaEliminada}$\n")
        else:
            print('\n¡Factura inexistente!\n')
    pendienteCobro = sum(facturas.values())
    print(f'Cantidad pendiente de cobro: {pendienteCobro}$')
    print(f'Cobrado hasta el momento: {acumuladorCobro}$\n')

# 6-Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:

# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, 
# permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

agenda = {
    'Pepe': 11000789,
    'Maria': 11987653,
    'Luis': 11667653,
    'Messi': 11234567,
    'Luisa': 11234568
}

opcion = 0
acumuladorCobro = 0
while opcion != '5':
    opcion = input("\n      --- Opciones ---"
                    "\n[1] Añadir/Modificar contacto"
                    "\n[2] Buscar contacto "
                    "\n[3] Borrar contacto "
                    "\n[4] Listar contactos" 
                    "\n[5] Salir "
                    "\nOpción: ")
    
    if(opcion == '1'):
        nombre = input("Nombre: ").capitalize()
        if(nombre in agenda): #Si ya existe, se modifica.
            print(f"\nNombre: {nombre} - Teléfono: {agenda[nombre]}")
            respuesta = input(f"¿Desea modificar el número de teléfono? [si/no]: ").lower()
            if(respuesta == 'si'):
                telefono = int(input("Nuevo teléfono: "))
                agenda[nombre] = telefono
                print("¡Modificación exitosa!")
        else: #Si no existe, se agrega.
            telefono = int(input("Teléfono: "))
            agenda[nombre] = telefono
            print("¡Se agrego el nuevo contacto!")          
        
    elif(opcion == '2'):
        txtBusqueda = input("Buscar contacto: ").capitalize()
        existe = False
        for i in agenda:
            if(i.startswith(txtBusqueda)):
                print(f"{i}: {agenda[i]}")
                existe = True
        if(not existe):
            print("¡Sin coincidencias!")
            
    elif(opcion == '3'):
        nombre = input("Nombre a borrar de la agenda: ").capitalize()
        if(nombre in agenda):
            respuesta = input(f"¿Desea borrar a {nombre}? [si/no]: ").lower()
            if(respuesta == 'si'):
                agenda.pop(nombre)
                print("¡Eliminación exitosa!")
        else:
            print("¡Contacto inexistente!")
            
    elif(opcion == '4'):
        print("\n- Lista de contactos -")
        for i in agenda:
            print(f'{i}: {agenda[i]}')