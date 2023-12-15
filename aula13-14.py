# AULA 13-14

import math #desde já rs

class FormaGeometrica:
    def __init__(self):
        pass

    @property
    def area(self):
        pass

    @property
    def perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self._lado = lado

    @property
    def area(self):
        return self._lado ** 2

    @property
    def perimetro(self):
        return 4 * self._lado

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def area(self):
        return self._base * self._altura

    @property
    def perimetro(self):
        return 2 * (self._base + self._altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @property
    def area(self):
        return math.pi * self._raio ** 2

    @property
    def perimetro(self):
        return 2 * math.pi * self._raio

class Triangulo(FormaGeometrica): #daqui em diante a IA ajudou :D
    def __init__(self, base, altura, lado_a, lado_b, lado_c):
        self.__base = float(base)
        self.__altura = float(altura)
        self.__lados = [float(lado_a), float(lado_b), float(lado_c)]

    @property
    def area(self):
        return 0.5 * self.__base * self.__altura

    @property
    def perimetro(self):
        return sum(self.__lados)

    @property
    def tipo_triangulo(self):
        tipos = ["Escaleno", "Isósceles", "Equilátero"]
        return tipos[self.__lados.count(self.__lados[0]) - 1]

#

lado_do_quadrado = 5
quadrado = Quadrado(lado_do_quadrado)
print(f"\nÁrea do quadrado: {quadrado.area}")
print(f"Perímetro do quadrado: {quadrado.perimetro}")

base_do_retangulo = 12
altura_do_retangulo = 6
retangulo = Retangulo(base_do_retangulo, altura_do_retangulo)
print(f"\nÁrea do retângulo: {retangulo.area}")
print(f"Perímetro do retângulo: {retangulo.perimetro}")

raio_do_circulo = 7
circulo = Circulo(raio_do_circulo)
print(f"\nRaio do círculo: {circulo.raio}")
print(f"Área do círculo: {circulo.area}")
print(f"Perímetro do círculo: {circulo.perimetro}")

triangulo = Triangulo(base=5.0, altura=8.0, lado_a=5.0, lado_b=5.0, lado_c=8.0)
print(f"\nÁrea do triângulo: {triangulo.area}")
print(f"Perímetro do triângulo: {triangulo.perimetro}")
print(f"Tipo do triângulo: {triangulo.tipo_triangulo}")

# Obs. já que o trapézio não é necessário eu não fiz :)
