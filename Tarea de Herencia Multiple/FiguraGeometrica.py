from abc import ABC, abstractmethod

class FiguraGeometrica:

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

    def __str__(self):
        return f'Ancho: [{self.ancho}]  Alto:[{self.alto}]'

    def _validar_valor(self, valor):  #  Nos permite restingir tambien los valores que so modifiquen fuera de la clase
        return True if 0 < valor < 10 else False
