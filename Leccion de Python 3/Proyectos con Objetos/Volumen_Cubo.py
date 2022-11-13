class Volumen_Prisma:

    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def Volumen(self):
        return self.base * self.altura * self.profundidad

base = float(input(f'Ingrese la Base: '))
altura = float(input(f'Ingrese la Altura: '))
profundidad = float(input(f'Ingrese la Profundidad: '))
prisma1 = Volumen_Prisma(base, altura, profundidad)

print(f'El Volumen del Prisma es: {prisma1.Volumen():.2f}')

base = float(input(f'Ingrese la Base: '))
altura = float(input(f'Ingrese la Altura: '))
profundidad = float(input(f'Ingrese la Profundidad: '))
prisma2 = Volumen_Prisma(base, altura, profundidad)

print(f'El Volumen del Prisma es: {prisma2.Volumen():.2f}')
