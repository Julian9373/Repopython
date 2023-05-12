class persona: 

    def __init__(self, nombre, edad, profesion, universidad):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.universidad = universidad 
     
    def saludar(self):
        print("Hola. Un gusto,  ")

    def presentarse(self):
        print("mi nombre es ", self.nombre, sep="")
        print("mi edad es", self.edad)
        print("mi prfesion es", self.profesion) 

    class estudiantes:

        def __init__(self, semestre, carrera, materias, universidad):
            self.semestre = semestre
            self.carrera = carrera
            self.materias = materias
            self.universidad = universidad

        def informacion(self):
            print("soy estudiante de la Universidad", self.universidad) 
            print("estudio", self.carrera)
            print("voy en", self.semestre, "semestre")
            print("estoy viendo", self.materias, "materias")
    
mi_persona = persona("julian", 21, "desarrollador de software", "del Rosario")
mi_persona.saludar()
mi_persona.presentarse()

mi_estudiante = persona.estudiantes(6, "ingenieria electronica", 4, "Del Rosario")
mi_estudiante.informacion()



