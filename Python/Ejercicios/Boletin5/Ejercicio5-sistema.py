class Asteroide():
    def __init__(self, masa, diametro, per_rotacion, per_traslación, distancia, excentricidad):
        self.__masa = masa
        self.__diametro = diametro
        self.__per_rotacion = per_rotacion
        self.__per_traslacion = per_traslación
        self.__distancia = distancia
        self.__excentricidad = excentricidad

    @property
    def masa(self):
        return self.__masa

    @masa.setter
    def masa(self, masa):
        self.__masa = masa

    @property
    def diametro(self):
        return self.__diametro

    @diametro.setter
    def diametro(self, diametro):
        self.__diametro = diametro

    @property
    def per_rotacion(self):
        return self.__per_rotacion

    @per_rotacion.setter
    def per_rotación(self, per_rotacion):
        self.__per_rotacion = per_rotacion

    @property
    def per_traslacion(self):
        return self.__per_traslacion

    @per_traslacion.setter
    def per_traslacion(self, per_traslacion):
        self.__per_traslacion = per_traslacion
    
    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

    @property
    def excentricidad(self):
        return self.__excentricidad

    @excentricidad.setter
    def escentricidad(self, excentricidad):
        self.__excentricidad = excentricidad

    def __gt__(self, asteroide):
        # vamos a compararlos por sus dimensiones
        if(self.masa > asteroide.masa and self.diametro > asteroide.diametro):
            return True

    def __str__(self):
        return str(self.masa) + ', ' + str(self.diametro) + ', ' + str(self.per_rotacion) + ', ' + str(self.per_traslacion) + ', ' + str(self.distancia) + ', ' + str(self.excentricidad)

class Planeta(Asteroide):
    def __init__(self, masa, diametro, per_rotacion, per_traslación, distancia, excentricidad, id_planeta, nombre):
        super().__init__(masa, diametro, per_rotacion, per_traslación, distancia, excentricidad)
        self.__id_planeta = id_planeta
        self.__nombre = nombre

    @property
    def id_planeta(self):
        return self.__id_planeta

    @id_planeta.setter
    def id_planeta(self, id_planeta):
        self.__id_planeta = id_planeta

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return super().__str__() + ', ' + str(self.id_planeta) + ', ' + self.nombre

class Satelite(Asteroide):
    def __init__(self, masa, diametro, per_rotacion, per_traslación, distancia, excentricidad, id_satelite, nombre):
        super().__init__(masa, diametro, per_rotacion, per_traslación, distancia, excentricidad)
        self.id_satelite = id_satelite
        self.__nombre = nombre

    @property
    def id_satelite(self):
        return self.__id_satelite

    @id_satelite.setter
    def id_satelite(self, id_satelite):
        self.__id_satelite = id_satelite

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return super().__str__() + ', ' + str(self.id_satelite) + ', ' + self.nombre

if __name__ == "__main__":

    planeta = Planeta(50,25,24,360,600,8,1,"tierra")
    satelite = Satelite(25,13,14,180,300,4,1,"luna")

    print(planeta.__str__())
    print(satelite.__str__())

    result = planeta.__gt__(satelite)

    print(result)