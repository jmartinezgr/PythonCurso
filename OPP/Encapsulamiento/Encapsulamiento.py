class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        return f'Esta persona se llama {self._nombre} {self._apellido} y tiene {self._edad} años '

    def __str__(self):
        return f'Persona {self._nombre + " " + self._apellido}'

    def __repr__(self):
        return f'Objeto tipo persona Nombre = {self._nombre} Apellido = {self._apellido} Edad = {self._edad}'

    def __del__(self):
        print(f'Objeto {self._nombre} de tipo persona eliminado')

if __name__ == "__main__":
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Juan Carlos'
    print(persona1.nombre)


