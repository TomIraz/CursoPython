# Herencia: cuando hay una sub-clase, la misma hereda las carateristicas de la clase

class PersonaH2(object):  # Clase Padre, la clase object es el padre de todas las clases en python

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona es: {self.nombre}, {self.apellido}, {self.edad}')

class Empleado(PersonaH2):  # Clase Hija, entre parentesis se coloca la clase padre
    def __init__(self, nombre, apellido, edad, sueldo):  # tendremos que agregar los parametros de la clase padre
        super().__init__(nombre, apellido, edad)  # super() nos permitira acceder a los metodos de la clase Padre
        self.sueldo = sueldo

empleado1 = Empleado('Tomas', 'Irazabal', 23, 5000)
empleado1.mostrar_detalle()
print(empleado1.sueldo)
