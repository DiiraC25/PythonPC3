class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Nombre:", self.nombre)
        print("Número de registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No asignadas")

    def set_age(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.notas.append(nota)

def main():
    nombre = input("Por favor, introduzca el nombre del alumno: ")
    num_registro = input("Por favor, introduzca el número de registro del alumno: ")
    
    alumno = Alumno(nombre, num_registro)

    alumno.set_age(int(input("Por favor, introduzca la edad del alumno: ")))

    num_notas = int(input("¿Cuántas notas desea asignar al alumno?: "))
    for i in range(num_notas):
        nota = float(input(f"Por favor, introduzca la nota {i+1} del alumno: "))
        alumno.set_nota(nota)

    print("\nInformación del alumno:")
    alumno.display()

if __name__ == "__main__":
    main()