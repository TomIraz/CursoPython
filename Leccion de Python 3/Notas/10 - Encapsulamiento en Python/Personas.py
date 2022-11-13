class Personas:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self. apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}')

    def __del__(self):  #Metodo Destructor ejecutado en PruebaPersonas1
        print(f'Persona: {self.nombre} {self.apellido}')

if __name__ == '__main__':  # De esta manera no se ejecutará desde otro archivo
    persona1 = Personas('Tomas', 'Irazabal', 23)
    persona1. nombre = 'Axel'
    persona1.apellido = 'Lopez'
    persona1.edad = 30
    persona1.mostrar_detalle()

print(__name__)  # esto lo pondremos en ambos archivos(PruebaPersonas y Personas)

# Esto nos muestra la diferencia de que cuando corremos desde Personas el if es verdadero y el obejeto se modifica
# Porque el nombre del archivo es el main
# Pero cuando se ejecuta el de pruebas el if es falso y desde aca no se ejecuta nada
