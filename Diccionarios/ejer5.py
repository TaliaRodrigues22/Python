#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas= {"2212": 15, "8040": 200, "3320": 100}
usuario = input("¿Quieres añadir una nueva factura [escriba NF], pagar una factura existente [escriba FE] o terminar[S]: ")
usuario = usuario.swapcase()
if  (usuario == "NF"):
    numerofac= input("Ingrese el numero de factura:")
    importe = int(input("Ingrese el importe a abonar: "))
    facturas.update({numerofac: importe})
    
    print(facturas)
elif (usuario == "FE"):
    numerofac= input("Ingrese el numero de factura:")
    print(f"Perfecto la factura: {numerofac} sera marcada como abonada")
    facturas.pop(numerofac)
    print(facturas)
else:
    print("hasta luego")