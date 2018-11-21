class Persona(): # los parentesis no son indispensables, se usan para la herencia principalmente
    # atributos ESTO NO ES NECESARIO PONERLO, PUES EN PYTHON SE INICIALIZA EN INIT
    __nombre = ""
    __edad = ""

    # constructor con parametros
    def __init__ (self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # metodos getters y setters
    # estilo java
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        return self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        return self.__edad = edad

    # con anotaciones
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    # metodos
    def Saludar(self):
        return "Hola"