from abc import ABC, abstractmethod

class FiguraGeometrica:
    def __init__(self,largo,ancho):
        self.ancho = ancho
        self.largo = largo

    @abstractmethod
    def calcularArea(self):
        pass

class Color:
    def __init__(self,color):
        self.color = color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.largo * self.ancho

