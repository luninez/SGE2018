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

