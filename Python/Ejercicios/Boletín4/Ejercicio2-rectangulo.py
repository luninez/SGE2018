class Punto():
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'

class Rectangulo():
    def __init__(self, p1, p2, p3, p4):  
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__p4 = p4
         
    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, p1):
        self.__p1 = p1

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, p1):
        self.__p2 = p2
    
    @property
    def p3(self):
        return self.__p3

    @p3.setter
    def p3(self, p3):
        self.__p3 = p3
    
    @property
    def p4(self):
        return self.__p4

    @p4.setter
    def p4(self, p4):
        self.__p4 = p4

    def superficie(self):
        ladoMenor = self.p1 - self.p2
        ladoMayor = self.p4 - self.p2
        return ladoMenor * ladoMayor

    def desplazar(self, x, y):
        self.p1.y = self.p1.y + y
        self.p1.x = self.p1.x + x
        
        self.p2.y = self.p2.y + y
        self.p2.x = self.p2.x + x

        self.p3.y = self.p3.y + y
        self.p3.x = self.p3.x + x

        self.p4.y = self.p4.y + y
        self.p4.x = self.p4.x + x

    def __str__(self):
        return str(self.p1) + ', ' + str(self.p2) + ', ' + str(self.p3) + ', ' + str(self.p4)

if __name__ == "__main__":

    p1 = Punto(1,5)
    p2 = Punto(1,1)
    p3 = Punto(5,5)
    p4 = Punto(5,1)

    rectangulo = Rectangulo(p1, p2, p3, p4)
    print(rectangulo.__str__())
    rectangulo.desplazar(2,2)
    print(rectangulo.__str__())