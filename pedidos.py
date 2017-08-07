import json

import personas

class Pedido:

    def __init__(self, fecha):
        self.fecha = fecha
        self.pedidos = []


class PedidoJefe:

    def __init__(self, jefe):
        self.jefe = jefe
        self.productos = []
        self.pagado = False
        self.precios = precios

    def __repr__(self):
        return "{} - Entregado: {} - Pagado: {}".format(
            self.jefe, self.entregado, self.pagado)

    @property
    def total(self):
        return sum(p.precio for p in self.productos)

    @property
    def entregado(self):
        for producto in self.productos:
            if not producto.entregado:
                return False
        return True

    def agregar_producto(self, producto):
        self.productos.append(producto)

    

    
class Producto:

    def __init__(self, nombre, precio, masa, unidad):
        self.nombre = nombre
        self.precio = precio
        self.masa = masa
        self.entregado = False        

    def __eq__(self, other):
        return self.nombre == other.nombre and \
               self.precio == other.precio and \
               self.masa == other.masa

    @property
    def producto_recibo(self):
        with open("productos.json", "r") as file:
            productos = json.load(file)
            try:
                return productos[self.nombre.lower()][str(self.masa)]
            except KeyError:
                return Exception("Producto no existe")

