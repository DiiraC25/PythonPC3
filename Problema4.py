class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

def main():
    largo = float(input("Por favor, introduzca el largo del rectángulo: "))
    ancho = float(input("Por favor, introduzca el ancho del rectángulo: "))
    mi_rectangulo = Rectangulo(largo, ancho)
    area = mi_rectangulo.calcular_area()
    print("El área del rectángulo es:", area)

if __name__ == "__main__":
    main()