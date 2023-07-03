class Persona:

    variable = 'Python<3Lover' #Variables de clase

    def __init__(self,nombre,edad):
        self.nombre = nombre #Variables de instancia
        self.edad = edad

    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

    @staticmethod
    def metodo_estatico():
        print(Persona.variable)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable)

    #El contexto dinamico puede acceder al contexto estatico
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable)

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__().replace("Persona","Empleado").replace("]",f', Sueldo: {self.sueldo}]')