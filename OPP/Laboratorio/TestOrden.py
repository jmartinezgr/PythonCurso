from OPP.Laboratorio.Computador import Computador
from OPP.Laboratorio.Monitor import Monitor
from OPP.Laboratorio.Orden import Orden
from OPP.Laboratorio.Raton import Raton
from OPP.Laboratorio.Teclado import Teclado

raton1 = Raton('HP', 'USB')
teclado1 = Teclado('HP', 'Bluetooth')
monitor1 = Monitor('Asus', 15)
Computadora = Computador('HP Pro Gamin', monitor1, teclado1, raton1)

raton1 = Raton('HP', 'USB')
teclado1 = Teclado('HP', 'Bluetooth')
monitor1 = Monitor('Asus', 15)
Computadora2 = Computador('HP Pro Gamin', monitor1, teclado1, raton1)

orden = Orden([Computadora,Computadora2])

print(orden)