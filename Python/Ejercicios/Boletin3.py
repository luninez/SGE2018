# Ejercicio 1
# lista = []
# continuar = input("Desea rellenar la lista: S/N ")
# while continuar.lower() == "s":
#     elemento = int(input("Inserta un numero: "))
#     lista.append(elemento)
#     continuar = input("Desea seguir rellenando: S/N ")

def sumarLista(lista):
    result = 0
    for i in range(0,len(lista)):
        result = result + lista[i]
    return result

# print(sumarLista(lista))

# Ejercicio 2
# primo = int(input("Introduzca un numero: "))

def numeroPrimo(primo):
    tope = int(primo/2)
    for i in range(2,tope):
        if (primo%i==0):
            return False
    return True

# print(numeroPrimo(primo))

# Ejercicio 3
def anioBisiesto():
    a = int(input("Introduce un año: "))
    if (a%4==0 and a%100!=0 or a%400==0):
        return True
    else:
        return False

# print("El año es bisiesto: "+str(anioBisiesto()))

# Ejercicio 4
from math import pi

def menu():
    print("CALCULADORA DE AREAS:")
    print("=====================")
    print("1. Area cuadrado")
    print("2. Area circulo")
    print("3. Area Triangulo")
    print("0. Area salir")

def cuadrado(lado):
    area = lado*lado
    return area

def circulo(radio):
    area = pi*radio**2
    return area

def triangulo(b,h):
    area = b*h/2
    return area

def areas():
    opcion = int(input("Escoja una opcion: "))
    if opcion == 0:
        return
    
    while opcion > 3 or opcion < 0:
        print("No has introducido una opcion correcta")
        opcion = int(input("Escoja una opcion: "))

    if (opcion == 1):
        lado = int(input("Introduce el lado: "))
        print("AREA: "+str(cuadrado(lado)))
    elif (opcion == 2):
        radio = float(input("Introduce el radio: "))
        print("AREA: "+str(circulo(radio)))
    elif(opcion == 3):
        b = float(input("Introduce la base del triangulo: "))
        h = float(input("Introduce la altura del triangulo: "))
        print("AREA: "+str(triangulo(b,h)))

# areas()

# Ejercicio 5
def cambio(precio,abonado):
    cambio = abonado - precio

    print("Su vuelta es:")

    if(cambio >= 20):
        contador = 0
        while cambio >= 20:
            cambio = cambio - 20
            contador = contador + 1
        print("Billetes de 20: "+str(contador))
    if(cambio >= 10):
        cambio = cambio - 10
        print("Billetes de 10: 1")
    if(cambio >= 5):
        cambio = cambio - 5
        print("Billetes de 5: 1")
    if(cambio >= 2):
        contador = 0
        while cambio >= 2:
            cambio = cambio - 2
            contador = contador + 1
        print("Monedas de 2: "+str(contador))
    if(cambio >= 1):
        cambio = cambio - 1
        print("Monedas de 1: 1")
    if(cambio >= 0.5):
        cambio = cambio - 0.5
        print("Monedas de 0.50: 1")
    if(cambio >= 0.2):
        contador = 0
        while cambio >= 0.2:
            cambio = cambio - 0.2
            contador = contador + 1
        print("Monedas de 0.20: "+str(contador))
    if(cambio >= 0.1):
        cambio = cambio - 0.1
        print("Monedas de 0.1: 1")
    if(cambio >= 0.05):
        cambio = cambio - 0.05
        print("Monedas de 0.05: 1")
    if(cambio >= 0.02):
        contador = 0
        while cambio >= 0.02:
            cambio = cambio - 0.02
            contador = contador + 1
        print("Monedas de 20: "+str(contador))

# abonado = float(input("Introduzca el dinero: "))
# precio = float(input("Introduzca el precio del refresco: "))
# cambio(precio,abonado)

# Ejercicio 6
def opcionesColores():
    print("1. Blanco")
    print("2. Negro")
    print("3. Azul")
    print("4. Amarillo")
    print("5. Rojo")

def ordenacion(arrayVotos, arrayColores):
    for j in range(len(arrayVotos)-1,0,-1):
        for i in range(j):
            if arrayVotos[i]<arrayVotos[i+1]:
                temp = arrayVotos[i]
                arrayVotos[i] = arrayVotos[i+1]
                arrayVotos[i+1] = temp

                temp = arrayColores[i]
                arrayColores[i] = arrayColores[i+1]
                arrayColores[i+1] = temp
    
    for i in range(len(arrayColores)):
        print(" - "+str(arrayColores[i])+" "+str(arrayVotos[i]))
        
def votarColores():
    blanco = 0
    negro = 0
    azul = 0
    amarillo = 0
    rojo = 0

    opcionesColores()
    opcion = int(input("Escoja un color: "))
    
    while opcion < -1 or opcion > 5:
        print("Esa opcion no existe.")
        opcionesColores()
        opcion = int(input("Escoja un color: "))

    while opcion >= -1 and opcion <= 5:
        if opcion == -1:
            arrayColores = ["Blanco","Negro","Azul","Amarillo","Rojo"]
            arrayVotos = []
            arrayVotos.append(blanco)
            arrayVotos.append(negro)
            arrayVotos.append(azul)
            arrayVotos.append(amarillo)
            arrayVotos.append(rojo)
            ordenacion(arrayVotos,arrayColores)
            return

        if opcion == 1:
            blanco = blanco + 1
        elif opcion == 2:
            negro = negro + 1
        elif opcion == 3:
            azul = azul + 1
        elif opcion == 4:
            amarillo = amarillo + 1
        elif opcion == 5:
            rojo = rojo + 1

        opcionesColores()
        print("Pulsa -1 para salir")
        opcion = int(input("Escoja un color: "))

votarColores()

