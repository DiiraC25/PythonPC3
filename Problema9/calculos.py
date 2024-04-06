import operaciones

def main():
    try:
        a = float(input("Por favor, introduzca el primer número: "))
        b = float(input("Por favor, introduzca el segundo número: "))

        resultado_suma = operaciones.suma(a, b)
        print("Resultado de la suma:", resultado_suma)

        resultado_resta = operaciones.resta(a, b)
        print("Resultado de la resta:", resultado_resta)

        resultado_producto = operaciones.producto(a, b)
        print("Resultado del producto:", resultado_producto)

        resultado_division = operaciones.division(a, b)
        print("Resultado de la división:", resultado_division)
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()