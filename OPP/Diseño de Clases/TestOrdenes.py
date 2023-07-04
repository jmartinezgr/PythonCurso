from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
orden1 = Orden([producto1, producto2])
orden2 = Orden([producto1,producto2])
print(orden1)
print(orden2)
producto3 = Producto('Calcetines',20.5)
orden1.agregar_producto(producto3)
print(orden1)