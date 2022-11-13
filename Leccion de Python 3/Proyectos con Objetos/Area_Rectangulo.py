class Area_Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Area(self):
        return self.base * self.altura

base = float(input(f'Ingrese la Base: '))
altura = float(input(f'Ingrese la Altura: '))
rectangulo1 = Area_Rectangulo(base, altura)

print(f'El Area del Rectangulo es: {rectangulo1.Area():.2f}')

base = float(input(f'Ingrese la Base: '))
altura = float(input(f'Ingrese la Altura: '))
rectangulo2 = Area_Rectangulo(base, altura)

print(f'El Area del Rectangulo es: {rectangulo2.Area():.2f}')
