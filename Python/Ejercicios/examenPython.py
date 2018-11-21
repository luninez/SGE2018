# Ejercicio 1
def es_palindromo(palabra):
    contador = 0
    for i in range(0, len(palabra),1):
        for j in range(len(palabra)-1,1,-1):
            if palabra[i] == palabra[j]:
                contador = contador + 1
    if contador == len(palabra):
        return True
    return False

# print(es_palindromo("radar"))
# print(es_palindromo("lucia"))

# Ejercicio 2
def histograma (lista):
    for i in range(0,len(lista)):
        print(str(lista[i])+": ")
        for j in range(0,lista[i]):
            print("*")

# histograma([1,2,3])
# histograma([8,4,5])

# Ejercicio 3
# def candidatos():
#     lista = []
#     num = int(input("Cuantos candidatos se presentan: "))
#     for i in range(1,num):
#         nombre = input("Escriba el nombre del candidato: ")
#         lista.append(nombre)
#     return lista

# def elegidos():
#     num = int(input("Cuantos candidatos podrán ser ganadores: "))

# def tipoVoto():
#     print("1. Voto nulo")
#     print("2. Voto en blando")
#     print("3. Voto correcto")

# def tipoCandidatos():
#     lista = candidatos()
#     for i in range(0,len(lista)):
#         print(str(i+1)+". "+str(lista[i]))

# def votaciones():
#     seguir = "s"
#     votonulo = 0
#     votoblanco = 0

#     while seguir == "s":
#         tipoVoto()
#         voto = int(input("Que tipo de voto es: "))
#         while voto < 1 or voto > 3:
#             print("Ese tipo de voto no existe")
#             tipoVoto()
#             voto = int(input("Que tipo de voto es: ")) 

#         if(voto == 1):
#             votonulo = votonulo + 1
#         elif(voto == 2):
#             votoblanco = votoblanco + 1
#         else:


# Ejercicio 4
def horas(hora,min,seg):
    segundosTotales = 0
    segundoHoras = 0
    segundoMinutos = 0
    
    if(hora >= 0):
        segundoHoras = hora * 3600
    if(min >= 0):
        segundoMinutos =  min * 60

    segundosTotales = segundoHoras + segundoMinutos + seg

    return segundosTotales

# print(horas(2,27,15))
# print(horas(1,1,1))

def segundos(seg):
    contador = 0
    if(seg >= 3600):
        while seg >= 3600:
            seg = seg - 3600
            contador = contador + 1
        print("Horas: "+str(contador))
    contador = 0
    if(seg >= 60):
        while seg >= 60:
            seg = seg - 60
            contador = contador + 1
        print("Minutos: "+str(contador))
    
        print("Segundos: "+str(seg))

# segundos(8835)
# segundos(3661)