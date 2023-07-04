class Monitor:

    contador_monitores = 0

    def __init__(self,marca,tamaño):
        Monitor.contador_monitores+=1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño

    @marca.setter
    def marca(self,new_marca):
        self._marca = new_marca

    @tamaño.setter
    def tamaño(self,new_tamaño):
        self.tamaño = new_tamaño

    @property
    def id_monitor(self):
        return self._id_monitor

    def __str__(self):
        return f'Monitor ID: {self._id_monitor}, Marca: {self._marca}, Tamaño {self._tamaño}'

