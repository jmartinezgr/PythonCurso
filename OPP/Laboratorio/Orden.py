import Computador

class Orden:

    contador_ordenes = 0

    def __init__(self,computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)

    def agregar_computadora(self,computadora):
        if isinstance(computadora,Computador):
            self._computadoras.append(computadora)
        else:
            print('Error: Tipo de dato invalido')

    def __str__(self):
        return f'Orden: {self._id_orden} :'+"\n".join(str(computador) for computador in self._computadoras)

