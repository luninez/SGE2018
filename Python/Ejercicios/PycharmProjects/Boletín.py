# Ejercicio 1
def numNaturales():
        num = 0
        while num <= 25:
                print(num)
                num = num + 1

# numNaturales()

# Ejercicio 2
def numImpares():
        num = 0
        while num <= 25:
                if num%2!=0:
                        print(num)
                num = num + 1

# numImpares()

# Ejercicio 3
def numPares():
        num = 40
        while num <= 60:
                if num%2==0:
                        print(num)
                num = num + 1

# numPares()

# Ejercicio 4
def numMasCuatro():
        num = 48
        while num <= 120:
                print(num)
                num = num + 4

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

sumaDecreciendo()

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
                print("El numero de par")
        else:
                print("El numero es impar")

num = input("Introduce un nume: ")
parImpar(num)
