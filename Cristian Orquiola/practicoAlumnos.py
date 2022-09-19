# Generar un diagrama de Flujo
# En una secundaria, los alumnos que estuvieron presentes,
# se han formado en una fila  por  orden de  llegada. Con  el
# objeto  de  llevar   registros  sobre  el  crecimiento  de  los
# adolescentes, el profesor necesita realizar ciertos cálculos
# sobre las alturas de los alumnos.
# En la secundaria hay 5 años, de primero a quinto (de 1 a 5), y
# de cada grado hay tres cursos (‘A’,’B’ y ‘C’).
# De cada alumno/a se conoce la siguiente información:
# ●Nombre (valor cadena).
# ●Altura en cm (valor entero).
# ●Grado (valor entero de 1 a 5).
# ●Curso al que pertenece (valor: ‘A’, ‘B’ o ‘C’).
# Para  ayudar  a al profesor,  se  te  pide  que  desarrolles  una
# aplicación,que  obtenga los siguientes resultados:
# a)  Por cada alumno/a, informar su nombre y su posición en
# la fila.
# Al finalizar, informar:
# b)La cantidad de alumnos en la fila, de cada curso.
# c)  La  altura del  alumno  más  alto  y  la  del  más  bajo  (se
# suponen  únicos),  indicando  en ambos casos, su posición
# en la fila.Considerar sólo a los alumnos de quinto grado.
# d) El promedio de las alturas, considerando a los alumnos de
# todos los años.
# Se ingresan datos de alumnos hasta que el usuario lo
# determine.



lista_alumnos = [("cristian",170,1,"a"),("Ariel",167,2,"b"),("Esteban",145,3,"c")]
def alumnos ():
    nombre_alumno = input("ingrese el nombre del alumno: ")
    altura_alumno = int(input("ingrese altura del alumno  en cm: "))
    grado_alumno = int(input("ingrese grado (valor entero de 1 a 5): "))
    curso_alumno = input("ingrese el curso  (‘A’,’B’ o ‘C’): ")
    total_datos = (nombre_alumno,altura_alumno,grado_alumno,curso_alumno)
    lista_alumnos.append(total_datos)

    agregar_alumnos= input("desea seguir agregando alumnos si/no :")

    if agregar_alumnos == "si":
        alumnos()

    else:
        print("los alumnos que agregamos son: ")

alumnos()
suma=0
for i in lista_alumnos:
    print(suma,":",i[0])
    suma +=1

cursoA, cursoB, cursoC = 0, 0, 0

for x in lista_alumnos:
    if x[3] == "a":
        cursoA += 1

    elif x[3] == "b":
        cursoB += 1

    elif x[3] == "c":
        cursoC += 1

print(f'El curso A tene :{cursoA} alumnos ,el curso B tiene:{cursoB} alumnos y el curso C tiene:{cursoC} alumnos ')

alturamin = []
alturas = []
def alumnoaltura ():
    for i in lista_alumnos:
        if i [2]==5:
         alturas.append(i[1])
    altura_max=max(alturas)
    for i in lista_alumnos:
        if i[2]==5 and i[1]==altura_max:
           posicion=lista_alumnos.index(i)
    print("el alumno mas alto del 5 año mide", altura_max,"y esta en la posicion",posicion)

    for i in lista_alumnos:
        if i [2]==5:
         alturamin.append(i[1])
    altura_min=min(alturamin)
    for i in lista_alumnos:
        if i[2]==5 and i[1]==altura_min:
           posicion2=lista_alumnos.index(i)
    print("y el alumno mas bajito del 5 año mide", altura_min,"y esta en la posicion",posicion2)
alumnoaltura()

# suma=0
# cantidades = len(lista_alumnos[1])
# def promedio():
#     for i in  lista_alumnos:
#         suma+= lista_alumnos[i][1]
#     promedio_total = suma/cantidades

#     print(promedio_total)

# promedio()


def PromedioAltura(lista_alumnos):
    acumulador = 0  
    for alumnos in lista_alumnos:
        acumulador += alumnos["alturas"]
    return acumulador/len(lista_alumnos)

PromedioAltura()


