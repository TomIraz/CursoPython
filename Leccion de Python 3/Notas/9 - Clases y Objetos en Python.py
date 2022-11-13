# Una clase es una plantilla de la cual podremos crear instancias u objetos
# Un objeto es una instancia de una clase las cuales posee atributos y metodos
# De esta manera podemos asignar caracteristicas como nombres y otras cosas
# Se recominda que el archivo .py se llame igual a la clase que va a almacenar
# Crear clases

class Persona: # las clases van en mayuscula para las primeras letras de cada palabra
    pass  # para indicar que no se procesará nada más

print(type(Persona))  # para averiguar si se creó bien el tipo de Persona (clase)


# Agregaremos atributos a los objetos (atributos de instancia)
# __init__(self): el metodo dunder se le llama al doble guion bajo y se usa cuando se trata de clases
class Persona:
    # El metodo init sirve para inicializar los atributos
    def __init__(self, nombre, apellido, edad):  # En este caso la variable, nombre es un parametro 
        self.nombre = nombre  # Atributo nombre, esta variable nombre es distinta a la de init es un atributo no un parametro
        # Del lado izquierdo son atributos y del derecho parametros de la clase
        self. apellido = apellido  # Atributo apellido
        self.edad = edad  # Atributo edad

persona1 = Persona('Tomás','Irazabal', 23)  # Lo que hace es mandar a llamar al metodo init de manera indirecta, creando el objeto
# persona1 es nuestro primer objeto o instancia que tien atributos como nombre, apellido y edad

print(persona1.nombre)  # de esta manera objeto.atributo imprimimos sus atributos
print(persona1.apellido)
print(persona1.edad)

# Otra manera de imprimir los atributos es:
print(f'Objeto Persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')

# Otra manera de modificar los atributos de los objetos es:
persona1.nombre = 'Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25

# Las Clases como ya dijimos poseen Metodos
# Metodos: Es el comportamiento que tendran nuestros objetos

class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self. apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):  # mostar_detalle es un Metodo
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}')  # la variable self solo se encuentra dentro de la definicion de nuestra clase
        # y se usa para acceder a los atributos de los objetos (solo dentro de la definicion de la clase)

persona1 = Persona('Tomas', 'Irazabal', 23)
persona2 = Persona('Juan','Martinez', 50)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Parametro Self (puede alterarse y usar cualquier otro parametro aunque es el default)
# También podemos pedir los atributos de un objeto mediante clase.metodo(objeto) usando la referencia Self
Persona.mostrar_detalle(persona1)

# Podemos agregar atributos a un objeto de manera que no cambie los atributos de toda la clase

persona1.telefono = '1143352584'
print(persona1.telefono)
# print(persona2.telefono) nos dira error


# Robustecer Metodo Init: Podemos usar *args para usar listas y tuplas o **kwargs para usar diccionario
class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self. apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}, {self.valores}, {self.terminos}')

persona3 = Persona('Matias', 'Irazabal', 28, '2346684', 1, 2, 3, m='manzana', p='pera')
persona3.mostrar_detalle()  # Output: Persona: Matias, Irazabal, 28, ('2346684', 1, 2, 3), {'m': 'manzana', 'p': 'pera'}
