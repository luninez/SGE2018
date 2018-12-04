from math import pi

class Figura():
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, lado):
        self.__lado = lado
 
    def area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio
 
    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        self.__radio= radio

    def area(self):
        return pi * self.radio * self.radio

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base= base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.altura= altura

    def area(self):
        return self.base * self.altura / 2.

if __name__ == "__main__":

    circulo = Circulo(10)
    print(circulo.area())