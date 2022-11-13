# Una clase es una plantilla de la cual podremos crear instancias u objetos
# Un objeto es una instancia de una clase las cuales posee atributos y metodos
# De esta manera podemos asignar caracteristicas como nombres y otras cosas
# Se recominda que el archivo .py se llame igual a la clase que va a almacenar
# Crear clases

class Persona:
    pass  # para indicar que no se procesará nada más

print(type(Persona))  # para averiguar si se creó bien el tipo de Persona (clase)


# Agregaremos atributos a los objetos (atributos de instancia)
# __init__(self): el metodo dunder se le llama al doble guion bajo y se usa cuando se trata de clases
class Persona:
    def __init__(self, nombre, apellido, edad):  # En este caso la variable, nombre es un parametro
        self.nombre = nombre  # Atributo nombre, esta variable nombre es distinta a la de init es un atributo no un parametro
        # Del lado izquierdo son atributos y del derecho parametros de la clase
        self. apellido = apellido  # Atributo apellido
        self.edad = edad  # Atributo edad

persona1 = Persona('Tomás','Irazabal', 23)  # Lo que hace es mandar a llamar al metodo init de manera indirecta, creando el objeto

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
persona1.mostrar_detalle()

# Podemos crear un archivo para ingresar objetos a nuestras clases, sin tener que modificar el archivo de la clase, ejemplo

# from Persona import Persona
#
# persona4 = Persona('Tomas','Irazabal', 25)
# persona4.mostrar_detalle()

print(__name__)  # esto lo pondremos en ambos archivos

# Si no queremos permitir que alguien más pueda hacer eso hacemos:
if __name__ == '__main__':  # De esta manera no se ejecutará desde otro archivo
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)
