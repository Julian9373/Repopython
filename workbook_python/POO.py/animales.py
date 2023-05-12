class animales:
    
    def __init__(self, tamaño, nombre, raza):
        self.__tamaño = tamaño
        self.__nombre = nombre
        self.__raza = raza 
    #getters 
    def get_tamaño(self):
          return self.__tamaño
    
    def get_nombre(self):
          return self.__nombre

    def get_raza(self):
          return self.__raza

    #setters

    def set_tamaño(self, tamaño):
          self.__tamaño = tamaño

    def set_nombre(self, nombre):
          self.__nombre = nombre 
    
    def set_raza(self, raza):
          self.__raza = raza

    def introduccion(self):
            print("Hola, ya sabemos que estas buscando un nuevo integrante para tu familia, ¿estás en busca de un perro o de un gato?: ")
    
    def siguiente(self):
          print("ahora tu, ¿estas buscando un gato? ")

class gato(animales):
      def __init__(self, tamaño, nombre, raza):
        super().__init__(tamaño, nombre, raza)


animal1 = animales("mediano", "tyke", "bulldog") 
animal1.introduccion()
respuesta_cate = input("¿quieres adopatar un perro? ")
if respuesta_cate == "si":
        print(f"Felicidades!! su nombre es {animal1.get_nombre()}, "  
              f"es de tamaño {animal1.get_tamaño()}, su raza no deberia importar pero este es un {animal1.get_raza()}")
        
animal1.siguiente()
animal2 = gato("pequeño", "Sky", "Angora")
respuesta_sig = input("Si / No: ") 
if respuesta_sig == "si":
    print(f"Felicidades!! su nombre es {animal2.get_nombre()}, es de tamaño {animal2.get_tamaño()}, su raza no deberia importar pero este es un {animal2.get_raza()}")      
         




