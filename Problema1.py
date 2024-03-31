def obtener_porcentaje_tanque(f):
    try:
        x, y = map(int, f.split('/'))
        if x <= 0 or y <= 0:
            raise ValueError("X e Y deben ser números enteros positivos")
        if x > y:
            raise ValueError("X debe ser menor o igual a Y")
        
        porcentaje = (x / y) * 100

        if porcentaje < 1:
            return "E"
        elif porcentaje > 99:
            return "F"
        else:
            return f"{int(round(porcentaje))}%"

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduzca una fracción válida.")
        return None
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. Por favor, introduzca una fracción válida.")
        return None

def main():
    while True:
        f = input("Por favor, introduzca una fracción en formato X/Y: ")
        resultado = obtener_porcentaje_tanque(f)
        if resultado:
            print("Cantidad de combustible en el tanque:", resultado)
            break

if __name__ == "__main__":
    main()