class bebidas:
    def __init__(self, energia, vitaminas, minerales, proteina):
        self.__energia = energia
        self.__vitaminas = vitaminas
        self.__minerales = minerales
        self.__proteina = proteina
    
    def get_energia(self):
        return self.__energia
    
    def get_vitaminas(self):
        return self.__vitaminas
    
    def get_minerales(self):
        return self.__minerales
    
    def get_proteina(self):
        return self.__proteina 
    
    def introduccion(self):
        print("Tenemos dos bebidas estrella, una para antes y otra para despues del entrenamiento ") 

class preentreno(bebidas):
    def __init__(self, energia, vitaminas, minerales, proteina):
      super().__init__(energia, vitaminas, minerales, proteina)

class postentreno(bebidas):
    def __init__(self, energia, vitaminas, minerales, proteina):
        super().__init__(energia, vitaminas, minerales, proteina)

pre = preentreno("150 calorias", "todas las vitaminas", "todos los minerales", "20 gramos de proteina ")
print(f"Esta bebida se llama PEM(PreEntrenoMax) y aporta {pre.get_energia()}, {pre.get_vitaminas()}, {pre.get_minerales()} y {pre.get_proteina()} ideales para comenzar con tu entrenamiento")

post= postentreno("150 calorias", "todas las vitaminas", "todos los minerales", "20 gramos de proteina ")
print(f"Esta bebida se llama POM(PostEntrenoMax) y aporta {post.get_energia()}, {post.get_vitaminas()}, {post.get_minerales()} y {post.get_proteina()} ideales para despues de tu entrenamiento")