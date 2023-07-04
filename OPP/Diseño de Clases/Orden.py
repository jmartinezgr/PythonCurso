from Producto import Producto

class Orden:
    contador_ordenes = 0
    def __init__(self,productos):
        Orden.contador_ordenes+=1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        return sum([producto.precio for producto in self._productos])

    def __str__(self):
        return f'Orden: {self._id_orden} Productos: '+'| '.join([str(producto) for producto in self._productos])

if __name__ == "__main__":
    producto1 = Producto('Camisa',100.00)
    producto2 = Producto('Pantalon', 150.00)
    orden1 = Orden([producto1,producto2])
    print(orden1)