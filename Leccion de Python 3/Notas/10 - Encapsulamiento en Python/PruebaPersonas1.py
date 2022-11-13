# Destructores

from Personas import Personas

print('Creacion de objetos'.center(30,'-'))  # Esto hara que se centre el objeto
persona1 = Personas('Tomas','Irazabal', 25)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(30,'-'))
del persona1

# Esto mandará a llamar al metodo destructor en la clase de Personas
