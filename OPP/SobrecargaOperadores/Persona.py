class Person:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return self.nombre +" "+other.nombre

    def __sub__(self, other):
        return self.edad - other.edad

if __name__ == '__main__':
    Persona1 = Person('Juan',10)
    Persona2 = Person('Karen',9)
    print(Persona1+Persona2)
    print(Persona1-Persona2)