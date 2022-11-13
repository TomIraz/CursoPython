from FiguraGeometrica import FiguraGeometrica
from Color import Color  # Podemos renombrar el nombre de la calse con as ejemplo: 'import Color as NewColor'

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):  # la variable ancho esta almacenada en la variable de lado
        FiguraGeometrica.__init__(self, lado, lado)  # la variable de lado solo nos sirve para incializar las variable de ancho y alto de la clase padre
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
