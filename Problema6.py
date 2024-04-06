class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        print(f'Se ha creado el producto: {self.nombre}')

    def __str__(self):
        return f'{self.nombre} ({self.año}) - Precio: {self.precio}'

class Catalogo:
    productos = []  # Esta lista contendrá objetos de la clase Producto

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, producto):  
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(producto)  

    def filtrar_por_año(self, año):
        print(f'Productos del año {año}:')
        for producto in self.productos:
            if producto.año == año:
                print(producto)

# Ejemplo de uso
p1 = Producto("Llanta", precio=100, año=2020)
p2 = Producto("Filtro de aceite", precio=20, año=2021)
p3 = Producto("Batería", precio=150, año=2019)

catalogo = Catalogo([p1, p2, p3])

# Mostrar el catálogo de productos actual
print("\nCatálogo actual:")
catalogo.mostrar()

# Agregar un nuevo producto al catálogo
catalogo.agregar(Producto("Faro", precio=80, año=2020))

# Mostrar el catálogo de productos después de agregar el nuevo producto
print("\nCatálogo después de agregar un nuevo producto:")
catalogo.mostrar()

# Filtrar productos por año
catalogo.filtrar_por_año(2020)