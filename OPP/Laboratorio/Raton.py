from DispositivoDeEntrada import DispositivoDeEntrada

class Raton(DispositivoDeEntrada):

    contador_ratones = 0 #Variable estatica

    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratones +=1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca,tipo_entrada)

    @property
    def id_raton(self):
        return self._id_raton

    def __str__(self):
        return f'Raton ID: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    raton1 = Raton('HP','USB')
    print(raton1)
    raton2 = Raton('Acer','Bluetooth')
    print(raton2)

