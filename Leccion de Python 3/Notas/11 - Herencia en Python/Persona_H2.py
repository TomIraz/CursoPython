class PersonaH2(object):

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):   # Para describir cada uno de los objetos
        return f'Persona: {self.nombre}, {self.edad}'  # Ahora la funcion print(objeto) Nos dira los atributos del objeto

class Empleado(PersonaH2):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f' Empleado: [Sueldo: {self.sueldo}] {super().__str__()}'

