from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())


# MRO - Method Resolution Order: Nos permite conocer la jerarquia de clases en la clase en la que la mandemos a llamar
print(Cuadrado.mro())