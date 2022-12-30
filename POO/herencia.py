#productos de la tienda de ropa
class Producto:
    def __init__(self,nombre: str,precio: int):
        self.nombre = nombre
        self.precio = precio
    
class Stock:
    def __init__(self,stock: int):
        self.stock = stock

class Ropa(Producto, Stock):
    def __init__(self,nombre: str,precio: int,stock: int, talla: str):
        Producto.__init__(self, nombre, precio)
        Stock.__init__(self,stock)
        self.talla = talla
        
    def nombre_producto(self):
        print('Nombre del producto: ', self.nombre)
        print('Precio: ', self.precio)
        print('Stock: ', self.stock)
        print('talla: ', self.talla)

# Creamos una nueva instancia de la clase Ropa
producto = Ropa('Camisa', 100, 10, 'M')
# Llamamos al método nombre_producto de la instancia de Ropa
producto.nombre_producto()