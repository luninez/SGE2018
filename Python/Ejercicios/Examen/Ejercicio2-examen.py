class Electrodomestico():
    def __init__(self, precio_base, color, peso, consumo_energetico):
        self.__precio_base = precio_base
        self.__color = color
        self.__peso = peso
        self.__consumo_energetico = consumo_energetico

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, precio_base):
        self.__precio_base = precio_base

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def consumo_energetico(self):
        return self.__consumo_energetico

    @consumo_energetico.setter
    def consumo_energetico(self, consumo_energetico):
        self.__consumo_energetico = consumo_energetico

    # @consumo_energetico.setter
    # def consumo_energetico(self, consumo_energetico):
    #     if(consumo_energetico <='a' and consumo_energetico >='f'):
    #         print('El consumo energetico no es correcto.')
    #         consumo = input('Por favor, inserte uno vaslido (a-f): ')
    #         return consumo_energetico(consumo)
    #     else:
    #         self.__consumo_energetico = consumo_energetico

    def comprobar_consumo_electrico(self, consumo_energetico):
        while(consumo_energetico <='a' and consumo_energetico >='f'):
            print('El consumo energetico no es correcto.')
            consumo_energetico = input('Por favor, inserte uno vaslido (a-f): ')

    def precio_final(self):
        if(self.consumo_energetico == 'a'):
            precio_consumo = self.precio_base + 100
        elif(self.consumo_energetico == 'b'):
            precio_consumo = self.precio_base + 80
        elif(self.consumo_energetico == 'c'):
            precio_consumo = self.precio_base + 60
        elif(self.consumo_energetico == 'd'):
            precio_consumo = self.precio_base + 50
        elif(self.consumo_energetico == 'e'):
            precio_consumo = self.precio_base + 30
        elif(self.consumo_energetico == 'f'):
            precio_consumo = self.precio_base + 10
        
        if(self.peso >= 0 and self.peso <= 19):
            precio_peso = self.precio_base + 10
        elif(self.peso >= 20 and self.peso <= 49):
            precio_peso = self.precio_base + 50
        elif(self.peso >= 50 and self.peso <= 79):
            precio_peso = self.precio_base + 80
        elif(self.peso >= 80):
            precio_peso = self.precio_base + 100

        return precio_consumo + precio_peso


class Lavadora(Electrodomestico):
    def __init__(self, carga, precio_base, color, peso, consumo_energetico):
        super().__init__(precio_base, color, peso, consumo_energetico)
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

class LavadoraIndustrial(Lavadora):
    def __init__(self, carga, precio_base, color, peso, consumo_energetico):
        super().__init__(precio_base, color, peso, consumo_energetico)
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    def comprobar_carga(self, carga):
        while(carga < 15 and carga > 50):
            print('La carga no es valida.')
            carga = int(input('Introduce una nueva: '))

    def precio_final(self):
        if(self.carga >= 30):
            return super().precio_final() + 50

if __name__ == "__main__":

    lavadora = Lavadora(5, 100, "blanco", 25, 'f')
    lavadoraIndustrial = LavadoraIndustrial(30, 100, "blanco", 25, 'f')

    