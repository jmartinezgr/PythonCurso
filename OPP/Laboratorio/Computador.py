from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computador:

    contador_computadora = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computador.contador_computadora +=1
        self._id_computador = Computador.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def id_computador(self):
        return self._id_computador

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self.raton

    def __str__(self):
        return f"""
{self._nombre}: {self._id_computador}
Monitor: {str(self._monitor)}
Teclado: {self._teclado}
Raton: {self._raton}
        """


if __name__ == '__main__':
    raton1 = Raton('HP','USB')
    teclado1 = Teclado('HP', 'Bluetooth')
    monitor1 = Monitor('Asus',15)
    Computadora = Computador('HP Pro Gamin',monitor1,teclado1,raton1)
    print(Computadora)