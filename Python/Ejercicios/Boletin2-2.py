def leerTelcado(texto):
    a = input(texto)
    return a

# COMO HAGO TODOS LOS EJERCICIOS EN EL MISMO FICHERO, TENGO TODOS LOS SCRIPT COMO SI FUERAN FUNCIONES
# PERO EL CODIGO ES EL MISMO QUE SI ESTUVIERAN FUERAS.

# Ejercicio 4
def mayorMultiploMenor():
    mayor = leerTelcado("Introduce el numero mayor: ")
    menor = leerTelcado("Introduce el numero menor: ")
    if mayor%menor==0:
        print('El %i si es multiplo de %i' %(mayor,menor))
    else:
        print('El %i no es multiplo de %i' %(mayor,menor))

# mayorMultiploMenor()

# Ejercicio 5
def compararTres():
    num1 = leerTelcado("Escribe el primer numero: ")
    num2 = leerTelcado("Escribe el segundo numero: ")
    num3 = leerTelcado("Escribe el tercer numero: ")
    
    if (num1!=num2 and num1!=num3 and num2!=num3):
        print("No hay ninguno igual")
    elif (num1==num2 and num2==num3):
        print("Los tres numeros son iguales")
    else:
        print("Uno de los tres es distinto")

# compararTres()

# Ejercicio 6
def anioBisiesto():
    a = int(leerTelcado("Introduce un año: "))
    if (a%4==0 and a%100!=0 or a%400==0):
        print(str(a)+" es un año bisiesto")
    else:
        print('%i no es un año bisiesto' %(a))

# anioBisiesto()

# Ejercicio 7
def ecuacionPrimerGrado():
    a = float(leerTelcado("Introdice a: "))    
    b = float(leerTelcado("Introdice b: "))
    if a != 0:
        x = (-b/a)
        print ('Solucion de la ecuacion: x=%4.3f  ' % (x))
    elif  a == 0 and  b != 0:
        print ('la ecuacion no tiene solucion:')
    else:
        print ('La ecuacion tiene infinitas soluciones. ')


# ecuacionPrimerGrado()

# Ejercicio 8
from math import sqrt

def ecuacionSegundoGrado():
    a = float(leerTelcado("Introdice a: "))    
    b = float(leerTelcado("Introdice b: "))
    c = float(leerTelcado("Introdice c: "))

    if a != 0:
        raiz = b**2-4*a*c
        if raiz < 0:
            print("La raiz es negativa, no se puede calcular")
        else:        
            x1 = ((-b+sqrt(b**2-4*a*c))/(2*a))
            x2 = ((-b-sqrt(b**2-4*a*c))/(2*a))
            print ('Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f ' %(x1,x2))
    elif b != 0:
        x = -c / b
        print ('Solucion de la ecuacion: x=%4.3f ' %(x))
    elif c != 0:
        print ('La ecuacion no tiene solucion.')
    else:
        print ('La ecuacion tiene infinitas soluciones. ')

# ecuacionSegundoGrado()

# Ejercicio 9
def areas():
    print("1. Area circulo")
    print("2. Area triangulo")
    texto = "Escoja una opcion: "

    respuesta = int(leerTelcado(texto))
    while respuesta != 1 or respuesta != 2:
        print(respuesta)
        print("No has introducido una opcion correcta")
        respuesta = leerTelcado(texto)

    if (respuesta == 1):
        radio = float(leerTelcado("Introduce el radio: "))
        area = (3.14)*radio**2
        print('el area del circulo es %.3f ' % area)
    else:
        b = float(leerTelcado("Introduce la base del triangulo: "))
        h = float(leerTelcado("Introduce la altura del triangulo: "))
        area = b*h/2
        print('El area del triángulo es: ', area)

areas()