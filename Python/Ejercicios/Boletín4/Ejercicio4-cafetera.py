class Cafetera():
    
    def __init__(self, capacidadMaxima):
        self.__capacidadMaxima = capacidadMaxima
        self.__cantidadActual = capacidadMaxima

    @property
    def capacidadMaxima(self):
        return self.__capacidadMaxima

    @capacidadMaxima.setter
    def capacidadMaxima(self, capacidadMaxima):
        self.__capacidadMaxima = capacidadMaxima

    @property
    def cantidadActual(self):
        return self.__cantidadActual

    @cantidadActual.setter
    def cantidadActual(self, cantidadActual):
        self.__cantidadActual = cantidadActual

    def llenar_cafetera(self):
        self.cantidadActual = capacidadMaxima

    def servir_cafe(self, cantidadServida):
        self.cantidadActual = self.cantidadActual - cantidadServida
        if(self.cantidadActual <= cantidadServida):
            self.cantidadActual = 0

    def vaciar_cafe(self):
        self.cantidadActual = 0

    def agregar_cafe(self, cantidadCafe):
        self.cantidadActual = self.cantidadActual + cantidadCafe
        if(self.capacidadMaxima < self.cantidadActual + cantidadCafe):
            self.cantidadActual = self.capacidadMaxima
            print('No puede agregar tanto cafe, sobresale.')
            return

    def __str__(self):
        return 'Cantidad Actual: ' + str(self.cantidadActual) + ', Capacidad maxima: ' + str(self.capacidadMaxima)

if __name__ == "__main__":

    cafetera = Cafetera(100)
    print(cafetera.__str__())
    cafetera.servir_cafe(10)
    print(cafetera.__str__())
    cafetera.agregar_cafe(50)
    print(cafetera.__str__())
    cafetera.vaciar_cafe()
    print(cafetera.__str__())
    cafetera.llenar_cafetera
    print(cafetera.__str__())