class CuerpoCeleste:
    def __init__(self, tamaño, nombre, tipo):
        self.__tamaño = tamaño
        self.__nombre = nombre
        self.__tipo = tipo
    
    # Getters
    def get_tamaño(self):
        return self.__tamaño
    
    def get_nombre(self):
        return self.__nombre
    
    def get_tipo(self):
        return self.__tipo
        
    
    # Setters
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    def introduccion(self):
        print("Hola, sabemos que estás buscando información sobre cuerpos celestes. ¿Estás interesado en un planeta o una estrella?")
    
    def siguiente(self):
        print("Ahora es tu turno, ¿estás buscando información sobre otro planeta?")

class Planeta(CuerpoCeleste):
    def __init__(self, tamaño, nombre, tipo, composicion):
        super().__init__(tamaño, nombre, tipo)
        self.__composicion = composicion
    def get_composicion(self):
        return self.__composicion

class Estrella(CuerpoCeleste):
    def __init__(self, tamaño, nombre, tipo, temperatura):
        super().__init__(tamaño, nombre, tipo)
        self.__temperatura = temperatura


cuerpo1 = CuerpoCeleste("Grande", "Júpiter", "Planeta")
cuerpo1.introduccion()
respuesta_cate = input("¿Estás interesado en un planeta? (si/no): ")
if respuesta_cate == "si":
    print(f"Felicidades!! El cuerpo celeste que has seleccionado es {cuerpo1.get_nombre()}. Es de tamaño {cuerpo1.get_tamaño()} y es un {cuerpo1.get_tipo()}.")
    cuerpo1.siguiente()

cuerpo2 = Planeta("Pequeño", "Mercurio", "Planeta", "Rocoso")
respuesta_sig = input("¿Quieres obtener más información sobre este planeta? (si/no): ")
if respuesta_sig == "si":
    print(f"Es excelente que quieras aprender!! El planeta que vamos a mirar es {cuerpo2.get_nombre()}. Es de tamaño {cuerpo2.get_tamaño()}, es un {cuerpo2.get_tipo()} y tiene una composición {cuerpo2.get_composicion()}.")