from HerenciaSimple import *
from HerenciaMultiple import Cuadrado

#Herencia y sobre escritura de metodos
persona1 = Persona('Juan',28)
print(persona1)
empleado1 = Empleado('Manuela',28,1000)
print(empleado1)

#Herencia Multiple
cuadrado1 = Cuadrado(2,"Rojo")
print(f'El area del cuadrado de color {cuadrado1.color} y de lado {cuadrado1.largo} es {cuadrado1.calcular_area()}')

#MEtodo de jerarquia de clases mro
print(Cuadrado.mro())

#Atributo de clase y metodo estatico
Persona.metodo_estatico()

#Metodo de clase
Persona.metodo_clase()

#Objeto accediendo al contexto estatico
persona1.metodo_instancia()