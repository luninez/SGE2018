class Fraccion(): 

    # getters y setters
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        self.__den = den

    # constructor con parametros
    def __init__ (self, num, den):
        self.__num = num
        self.__den = den
        if (den == 0):
            self.__den = 1
        
    # metodos
    def mcd(self, a, b):
        resto = 0
        while(b > 0):
            resto = b
            b = a % b
            a = resto
        return int(a)

    def mcm(self, a, b):
        result = int((a * b) / self.mcd(a, b))
        return result

    def sumar(self, frac2):
        if(self.__den != frac2.__den):
            nmcm = self.mcm(self.__den, frac2.__den)

            x = int(nmcm/self.__den)
            num1 = x * self.__num

            y = int(nmcm/frac2.__den)
            num2 = y * frac2.__num

            suma = num1 + num2
            return self.__init__(suma, nmcm)
        else:
            suma = self.__num + frac2.__num
            return self.__init__(suma, self.den)
        

    def restar(self, frac2):
        if(self.__den != frac2.__den):
            nmcm = self.mcm(self.__den, frac2.__den)

            x = int(nmcm/self.__den)
            num1 = x * self.__num

            y = int(nmcm/frac2.__den)
            num2 = y * frac2.__num

            resta = num1 - num2
            return self.__init__(resta, nmcm)
        else:
            resta = self.__num - frac2.__num
            return self.__init__(resta, self.__den)

    def multiplicar(self, frac2):
        num = self.__num * frac2.__num
        den = self.__den * frac2.__den
        return self.__init__(num, den)

    def dividir(self, frac2):
        num = self.__num * frac2.__den
        den = self.__den * frac2.__num
        return self.__init__(num, den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

if __name__ == "__main__":

    frac1 = Fraccion(2,3)
    frac2 = Fraccion(4,5)

    frac1.sumar(frac2)
    print(frac1.__str__())

    frac1.dividir(frac2)
    print(frac1.__str__())