class Vehiculo:

    def __init__(self, color, ruedas: int):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas ' + str(self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return 'Coche: [Color: ' + self.color + ' Velocidad(km/hr): ' + str(self.velocidad) + ']'

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return 'Bicicleta: [Color: ' + self.color + ', Tipo: ' + self.tipo + ']'
