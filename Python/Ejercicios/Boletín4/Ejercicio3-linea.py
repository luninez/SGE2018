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

class Linea():
    def __init__(self, p1, p2):  
        self.__p1 = p1
        self.__p2 = p2
         
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
   
    def mueve_derecha(self, x):
        self.p1.x = self.p1.x + x
        
        self.p2.x = self.p2.x + x

    def mueve_izquierda(self, x):
        self.p1.x = self.p1.x - x
        
        self.p2.x = self.p2.x - x

    def mueve_arriba(self, y):
        self.p1.y = self.p1.y + y
        
        self.p2.y = self.p2.y + y

    def mueve_abajo(self, y):
        self.p1.y = self.p1.y - y
        
        self.p2.y = self.p2.y - y

    def __str__(self):
        return '[(' + str(self.p1) + '),(' + str(self.p2) + ')]'

if __name__ == "__main__":

    p1 = Punto(1,1)
    p2 = Punto(1,4)

    linea = Linea(p1, p2)

    print(linea.__str__())

    linea.mueve_arriba(3)

    print(linea.__str__())
