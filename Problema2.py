def obtener_calificaciones():
    while True:
        calificaciones = input("Por favor, introduzca las calificaciones separadas por comas: ")
        try:
            calificaciones_lista = calificaciones.split(',')
            calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Por favor, asegúrese de que todas las calificaciones sean números enteros.")

def main():
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)

if __name__ == "__main__":
    main()