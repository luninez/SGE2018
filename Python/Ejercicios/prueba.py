# Ejercicio 13
def multiploTres():
    contador = 0
    num = 0
    for i in range(0,101):
        if i%3==0:
            contador = contador + 1
            num = num + i
    
    print(f"Contador: {contador}")
    print(num)

multiploTres()