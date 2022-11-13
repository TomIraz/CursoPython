# Creamos un archivo para ingresar objetos a nuestras clases
from Personas import Personas

persona1 = Personas('Tomas','Irazabal', 25)
persona1.mostrar_detalle()

# Un problema es que al correr este .py también se ejeucta el archivo de la clase
# Para corregir esto haermos algo
# Usaremos print(__name__) para dar a entender cuál archivo se está imprimiendo

print(__name__)  # esto lo pondremos en ambos archivos

# __main__  # Main es siempre el archivo desde donde se corrio el codigo, en este caso PruebaPersonas.py

# Al correr el codigo se ejecutará solo este archivo gracias al if que hay en la clase: Personas

