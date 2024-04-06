import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"

    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)

    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return math.sqrt(dx**2 + dy**2)


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()


# Ejemplo de uso
punto1 = Punto(2, 3)
punto2 = Punto(5, 7)
rectangulo = Rectangulo(punto1, punto2)

print("Base del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())

print("Punto 1 está en el", punto1.cuadrante())
print("Punto 2 está en el", punto2.cuadrante())

vector_resultante = punto1.vector(punto2)
print("Vector resultante entre punto1 y punto2:", vector_resultante)

distancia_entre_puntos = punto1.distancia(punto2)
print("Distancia entre punto1 y punto2:", distancia_entre_puntos)