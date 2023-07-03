from OPP.Encapsulamiento.Encapsulamiento import Persona

print('Creacion de objetos'.center(40,'-'))
persona = Persona('Karla','Gomez',40)

print('Metodo str de objetos'.center(40,'-'))
print(persona)

print('Metodo representacion de objetos'.center(40,'-'))
print(repr(persona))

print('Eliminacion objetos'.center(40,'-'))
del persona

