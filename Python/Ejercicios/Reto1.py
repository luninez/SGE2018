array = []

for i in range (2, 22):
    array.append(i)

def esPrimo(p):
    for i in range(2,p):
        if (p%i)==0:
            # es divisible
            return False
    return True

def maximoDivisor(p):
    q = 0
    for i in range (1, p):
        if (p%i == 0):
         q = i
    return q
    
p = 1
print(array)
for i in range (0, len(array)):
    p = p - 1
    print("Parte de la poscion: "+str(p))
    for j in range (p, len(array)):
        print("Array["+str(j)+"] = "+str(array[j]))
        if (esPrimo(array[j]) == False):
            array[j] = int(array[j] / maximoDivisor(array[j]))
            array[j-1] = int(array[j-1] + array[j])
            p = j
            print(array)
            print(p)
            break