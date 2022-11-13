
# Variables de Clases: Son variables que se compartiran con todos los objetos de la clase, se asocian con las Clases

class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):  # Variable de instancia, se asocia con los objetos
        self.variable_instancia = variable_instancia

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)  # Podemos ver que desde el objeto podemos recuperar la variable de clase

miClase2 = MiClase('Nuevo valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)  # Podemos ver que la variable de clase es igual para todos
