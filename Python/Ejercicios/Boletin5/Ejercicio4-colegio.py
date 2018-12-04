class Direccion():

    def __init__ (self, calle, codigo_postal, ciudad, provincia):
        self.__calle = calle
        self.__codigo_postal = codigo_postal
        self.__ciudad = ciudad
        self.__provincia = provincia

    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, calle):
        self.__calle = calle

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @property
    def codigo_postal(self):
        return self.__codigo_postal

    @codigo_postal.setter
    def codigo_postal(self, codigo_postal):
        self.__codigo_postal = codigo_postal

    @property
    def provincia(self):
        return self.__provincia

    @provincia.setter
    def provincia(self, provincia):
        self.__provincia = provincia

    def __str__(self):
        return self.calle + ' ' + str(self.codigo_postal) + ' ' + self.ciudad + ' ' + self.provincia

class Persona():
    def __init__ (self, nombre, apellidos, dni, direccion):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__direccion = direccion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' ' + str(self.dni) + ' ' + str(self.__direccion)

class Estudiante(Persona):
    def __init__ (self, nombre, apellidos, dni, direccion, id_estudiante):
        super(Estudiante, self).__init__(nombre, apellidos, dni, direccion)
        self.__id_estudiante = id_estudiante

    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @id_estudiante.setter
    def id_estudiante(self, id_estudiante):
        self.__id_estudiante = id_estudiante

    def __str__(self):
        return str(self.id_estudiante) + ' ' + super().__str__()

class Profesor(Persona):
    def __init__ (self, nombre, apellidos, dni, direccion, id_despacho):
        super(Profesor, self).__init__(nombre, apellidos, dni, direccion)
        self.__id_despacho = id_despacho

    @property
    def id_despacho(self):
        return self.__id_despacho

    @id_despacho.setter
    def id_despacho(self, id_despacho):
        self.__id_despacho = id_despacho

    def __str__(self):
        return str(self.id_despacho) + ' ' + super().__str__()

if __name__ == "__main__":

    presona = Persona("Pepe","Pérez Pérez","12345678A", Direccion("calle","41010","Sevilla","Sevilla"))
    print(presona.__str__())

    estudiante = Estudiante("Pepe","Pérez Pérez","12345678A", Direccion("calle","41010","Sevilla","Sevilla"),1)
    print(estudiante.__str__())