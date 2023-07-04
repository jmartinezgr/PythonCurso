from DispositivoDeEntrada import DispositivoDeEntrada

class Teclado(DispositivoDeEntrada):

    contador_teclados = 0 #Variable Estatica

    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclados+=1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca,tipo_entrada)

    @property
    def id_teclado(self):
        return self._id_teclado

    def __str__(self):
        return f'Teclado ID: {self._id_teclado}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('HP','Bluetooth')
    print(teclado1)
    teclado2 = Teclado('Asus','USB')
    print(teclado2)