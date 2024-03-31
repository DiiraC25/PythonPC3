import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

def main():
    radio = float(input("Por favor, introduzca el radio del círculo: "))
    mi_circulo = Circulo(radio)
    area = mi_circulo.calcular_area()
    print("El área del círculo es:", area)

if __name__ == "__main__":
    main()