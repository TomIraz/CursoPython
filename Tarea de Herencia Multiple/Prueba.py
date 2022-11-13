from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(6, 'Rojo')
cuadrado2 = Cuadrado(2, 'Azul')
cuadrado1.alto = 2
cuadrado1.ancho = 2

print(f'Cuadrado1:{cuadrado1}')
print(f'El Area de Cuadrado1 es: {cuadrado1.area()}')
print(f'Cuadrado2:{cuadrado2}')
print(f'El Area de Cuadrado2 es: {cuadrado2.area()}')

print(f'Rectangulo'.center(30,'-'))
rectangulo1 = Rectangulo(5, 7, 'Amarillo')

print(f'Rectangulo1: {rectangulo1}')
print(f'El Area de Rectangulo1 es: {rectangulo1.area()}')

