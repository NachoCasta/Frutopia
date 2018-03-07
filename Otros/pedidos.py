import json

import personas

class Pedido:

    def __init__(self, fecha):
        self.fecha = fecha
        self.pedidos = []

    def productos_distintos(self):
        productos = []
        for pedido in self.pedidos:
            for producto in pedido.productos_distintos():
                producto_recibo = producto.producto_recibo
                if producto_recibo not in productos:
                    productos.append(producto_recibo)
        return productos


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

    def productos_distintos(self):
        productos = []
        for producto in self.productos:
            if producto not in productos:
                productos.append(producto)
        return productos
        

    
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

