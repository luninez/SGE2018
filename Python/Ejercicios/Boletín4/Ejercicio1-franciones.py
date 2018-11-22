class fraccion(): 

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
    def mcm(self,A,B):
        C = B
        while(C != 0):
            C= A%B
            A = B
            B = C             
        return (A*B)/B

    def sumar(self, frac1, frac2):
        if(frac1.__den != frac2.__den):
            nmcm = self.mcm(frac1.__den, frac2.__den)

            x = nmcm/frac1.__den
            num1 = x * frac1.__num

            y = nmcm/frac2.__den
            num2 = y * frac2.__num

            num = num1 + num2
            return fraccion(suma, nmcm)
        else:
            suma = frac1.__num + frac2__num
            return fraccion(suma, frac1.__den)
        

    def restar(self, frac1, frac2):
        if(frac1.__den != frac2.__den):
            nmcm = self.mcm(frac1.__den, frac2.__den)

            x = nmcm/frac1.__den
            num1 = x * frac1.__num

            y = nmcm/frac2.__den
            num2 = y * frac2.__num

            resta = num1 - num2
            return fraccion(resta, nmcm)
        else:
            resta = frac1.__num - frac2.__num
            return fraccion(resta, frac1.__den)

    def multiplicar(self, frac1, frac2):
        num = frac1.__num * frac2.__num
        den = frac1.__den * frac2.__den
        return fraccion(num, den)

    def dividir(self, frac1, frac2):
        num = frac1.__num * frac2.__den
        den = frac1.__den * frac2.__num
        return fraccion(num, den)