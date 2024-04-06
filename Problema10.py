from Problema3 import Circulo
from Problema4 import Rectangulo

def calcular_area_circulo():
    radio = float(input("Por favor, introduzca el radio del círculo: "))
    mi_circulo = Circulo(radio)
    area = mi_circulo.calcular_area()
    print("El área del círculo es:", area)

def calcular_area_rectangulo():
    largo = float(input("Por favor, introduzca el largo del rectángulo: "))
    ancho = float(input("Por favor, introduzca el ancho del rectángulo: "))
    mi_rectangulo = Rectangulo(largo, ancho)
    area = mi_rectangulo.calcular_area()
    print("El área del rectángulo es:", area)

def calcular_area_cuadrado():
    lado = float(input("Por favor, introduzca el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", area)

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()