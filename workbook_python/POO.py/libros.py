class libro:
    def __init__(self, titulo, precio, autor):
        self.__titulo = titulo
        self.__precio = precio
        self.__autor = autor

    def get_info(self):
        return f"\n Titulo: {self.__titulo}\n Precio: {self.__precio}\n Autor: {self.__autor}\n Paginas: 900"
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_autor(self, autor):
        self.__author = autor
    def get_titulo(self):
        return self.__titulo
    def get_precio(self):
        return self.__precio
    def get_autor(self):
        return self.__autor

libro1 = libro("El renacuajo paseador", "60.000", "Rafael Pombo")

print(libro1.get_info())

class novela(libro):
    def __init__(self, titulo, precio, autor, num_paginas):
        super().__init__(titulo, precio, autor)
        self.num_paginas = num_paginas

    def get_info(self):
        return f"\n Titulo: {self.get_titulo()}\n Precio: {self.get_precio()}\n Autor: {self.get_autor()}\n Numero de paginas: {self.num_paginas}"


comic1 = novela("100 años de soledad", 100000, "Gabriel Garcia Marquez", 500)

print(comic1.get_info())
