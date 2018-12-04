class Libro():
    def __init__(self, isbn, title, autor, num_pages):
        self.__isbn = isbn
        self.__title = title
        self.__autor = autor
        self.__num_pages = num_pages

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def num_pages(self):
        return self.__num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        self.__num_pages = num_pages

    def __eq__(self, libro):
        return self.num_pages == libro.num_pages

    def __ge__(self, libro):
        return self.num_pages >= libro.num_pages

    def __le__(self, libro):
        return self.num_pages <= libro.num_pages

    def __cmp__(self, libro):
        if(self.__eq__(libro)):
            return 0
        elif(self.__ge__(libro)):
            return 1
        else:
            return -1


    def __str__(self):
        return 'El libro con' + str(self.isbn) + ' creado por ' + str(self.autor) + ' tiene ' + str(self.num_pages) + ' páginas'

if __name__ == "__main__":

    libro1 = Libro(70281369,"Mil soles esplendidos","Laura Gallego",80)
    libro2 = Libro(80213594,"Desde mi cielo","Anonimo",100)

    print(libro1.__cmp__(libro2)) 