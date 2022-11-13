# Clases Abstractas: olbiga a las clases hijas a implementar metodos de las clases Padres
# Si en una clase agregamos un metodos abstracto --> toda la clase se vuelve abstracta
# De las clases abstractas no se pueden crear instancias u objetos
# También se puede utilizar para obligar a utilizar el metodo setter para que no se pueda modificar una vez inicializado
# el objeto

# Convertir una clase en clase abstracta

# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'El valor de Alto es erroneo: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'El valor de Ancho es erroneo: {ancho}')

    @abstractmethod
    def calcular_area(self):
        pass  # Al ser un metodo abstracto no puede tener ninguna implementacion asi que usamos pass
        # que indica que no contiene ninguna implementacion

    def __str__(self):
        return f'Ancho: [{self.ancho}]  Alto:[{self.alto}]'

    def _validar_valor(self, valor):  #  Nos permite restingir tambien los valores que so modifiquen fuera de la clase
        return True if 0 < valor < 10 else False
