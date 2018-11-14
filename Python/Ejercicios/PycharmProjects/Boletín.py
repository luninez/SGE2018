# Ejercicio 1
def numNaturales():
        for i in range(0,26):
                print(i)

# numNaturales()

# Ejercicio 2
def numImpares():
        for i in range(0,26):
                if i%2!=0:
                        print(i)

# numImpares()

# Ejercicio 3
def numPares():
        for i in range(0,26):
                if i%2==0:
                        print(i)

# numPares()

# Ejercicio 4
def numMasCuatro():
        for i in range(48,121, 4):
                print(i)

# numMasCuatro()

# Ejercicio 5 & 6
def suma():
        num = 0
        for i in range(51):
                num = num + i

        print(num)  

# suma()

# Ejercicio 7
def multiplicar():
        num = 0
        for i in range(21):
                num = num + i

        print(num)  

# multiplicar()

# Ejercicio 8
def sumaDecreciendo():
        num = 10
        for i in range(10,0):
                num = num + i

        print(num)  

# sumaDecreciendo()

# Ejercicio 9
def sumaDecreciendoImpares():
        num = 10
        for i in range(10,0):
                num = num + i
                if num%2==0:
                        print(num)
                 

# sumaDecreciendoImpares()

# Ejercicio 10
def parImpar(num):
        if num%2==0:
                print("El numero es par")
        else:
                print("El numero es impar")

#num = input("Introduce un numero: ")
# parImpar(num)

# Ejercicio 11
def dobleSuma():
    par = 0
    impar = 0
    for i in range(0,101):
        if i%2==0:
            par = par + i
        else:
            impar = impar + i

    print(par)
    print(impar)

# dobleSuma()

# Ejercicio 12
def numTeclado(min, max):
        par = 0
        contador = 0
        contadorPares = 0
        for i in range(min,max+1):
                contador = contador + 1
                print(i)
                if i%2==0:
                        contadorPares = contadorPares + 1
                        par = par + i
        
        print(f"Contador: {contador}")
        print(f"Contador pares: {contadorPares}")
        print(par)

# min = input("Introduce el numero más pequeño: ")
# min = int(min)
# max = input("Introduce el numero más grande: ")
# max = int(max)
# numTeclado(min, max)

# Ejercicio 13
def mulriplosTres():
        contador = 0
        for i in range(1,101):
                if i%3==0:
                        print(i)
                        contador = contador + 1
        
        print(f"Contador: {contador}")

# mulriplosTres()

# Ejercicio 14
def multiploDosTres(max):
        suma = 0
        contador = 0
        for i in range(1,max+1):
                if i%2==0 and i%3==0:
                        print(i)
                        contador = contador + 1
                        suma = suma + i
        
        print(f"Contador: {contador}")
        print(f"Suma: {suma}")

# max = input("Introduce un numero: ")
# max = int(max)
# multiploDosTres(max)

# Ejercicio 15
def dosOpciones(a,b):
        suma = 0
        if a >= b:
                for i in range(10,51,4):
                        suma = suma + i
                print(suma)
        elif a/b <= 30:
                result = a**2+b**2
                print(result)
        else:
                print("No es ninguna opcion")
        
# a = input("Introduce a: ")
# a = int(a)
# b = input("Introduce b: ")
# b = int(b)       
# dosOpciones(a,b)

#Ejercicio 16
def tresOpciones(a,b,c):
        result = 0
        suma = 0
        if a/b > 30:
                result = a/c*b**3
                print(f"result: {result}")
        elif a/b <= 30:
                for i in range(2,31):
                        suma = suma + i**2
                print(f"suma: {suma}")

a = input("Introduce a: ")
a = int(a)
b = input("Introduce b: ")
b = int(b) 
c = input("Introduce c: ")
c = int(c)      
tresOpciones(a,b,c)