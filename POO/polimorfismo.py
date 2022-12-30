#productos de la tienda de ropa
class Producto:
    def __init__(self,nombre: str,precio: int):
        self.nombre = nombre
        self.precio = precio
    
class Stock:
    def __init__(self,stock: int):
        self.stock = stock
        
    def consultar_tipo(self):
        print("Stock")

class Ropa(Producto, Stock):
    def __init__(self,nombre: str,precio: int,stock: int, talla: str):
        Producto.__init__(self, nombre, precio)
        Stock.__init__(self,stock)
        self.talla = talla
    
    def consultar_tipo(self):
        print("Ropa")
        
    def nombre_producto(self):
        print('Nombre del producto: ', self.nombre)
        print('Precio: ', self.precio)
        print('Stock: ', self.stock)
        print('talla: ', self.talla)
        
# instanciar polimorfismo
stock = Stock(10)
ropa = Ropa('Camisa', 100, 10, 'M')

def mostrar_tipo(objeto: str) -> str:
    objeto.consultar_tipo()
    
mostrar_tipo(ropa)
mostrar_tipo(stock)