# Encapsulamiento: Advertir el acceso de atributos fuera de nuestra clase, usando el _
# Con doble guion bajo __ se prohibe completamente el acceso al atributo fuera de la calse

class Personas:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre}, {self.apellido}, {self.edad}')  # Estamos accediendo desde adentro de la clase

persona1 = Personas('Tomas', 'Irazabal', 23)
persona1._nombre = 'Matias'  # indicamos que no deberiamos acceder al atributo, a esto se le llama encapsulamiento

persona1.mostrar_detalle()

# Metodos Get y Set
# Get = Obetener/Recuperar los atributos de nuestra clase
# Set = Colocar/Modificar los atributos de nuestra clase
# Decoradores: Sirven para asegurarnos que no accedan a atributos con _ modificando el comportamiento de los metodos

class Personas:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property  # Este es el decorador que no permitira el acceso a _atributo obligandonos a usar el Get
    def nombre(self):  # Esto es un Get
        return self._nombre

    @nombre.setter  # Este decorador sirve para mostrar que sera un metodo de tipo set asociado al atributo
    def nombre(self, nombre):  # Esto es un Set para poder moificar nuestro atributo
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre}, {self.apellido}, {self.edad}')  # Estamos accediendo desde adentro de la clase

persona1 = Personas('Tomas', 'Irazabal', 23)

print(persona1.nombre)  # No Corresponde usar parentesis 'print(persona1.nombre())'
# porque está el decorador haciendo que el metodo se comporte como un atributo

persona1.nombre = 'Matias'
print(persona1.nombre)

# From: Nos permite crear un archivo para ingresar objetos a nuestras clases, sin tener que modificar el archivo de la clase

# Para verlo ir a PruebaPersonas.py

# Destructores: Al eliminar un objeto se manda a llamar este metodo de manera automatica

# Para verlo ir a PreubaPersonas1.py
