# Operadores
# suma:+
# Resta:-
# Negacion:-
# Multipiclacion:*
# Exponente:**
# Division:/
# Division Entera://
# Modulo:% ----> calcula el residuo de una division

# Ejercicio: Calculo de Area y Perimetro
alto = int(input('El Alto es: '))
ancho = int(input('El Ancho es: '))
perimetro = alto * 2 + ancho * 2
area = alto * ancho
print(f'El Perimetro es: {perimetro}')
print(f'El Area es: {area}')

# Incremento
mivariable = 5
mivariable = mivariable + 1
print(mivariable)

# Comparacion
# Igual: ==
# Distinto: =!
# Mayor: >
# Menor:<

a = 5
b = 4

resultado = a == b
print(f'Son Iguales == : {resultado}')

resultado = a != b
print(f'Son Distintos : {resultado}')

resultado = a > b
print(f'a es Mayor a b : {resultado}')

resultado = a < b
print(f'a es Menor a b: {resultado}')

# Ejercicio: Resultado par o impar
a = int(input('Valor de A: '))
resto: bool = a % 2 == 0
if resto:
    print(f'{a} es Par')
else:
    print(f'{a} es Impar')

# Ejercicio: Eres mayor o menor de edad?
edad = int(input('Mi Edad es: '))
if edad >= 18:
    print(f'Eres mayor de edad')
else:
    print(f'Eres menor de edad')

# Operadores:
# and: Devuelve True si ambos operadores son True ----> a and b
# or: Devuelve True si algunos operadores son True ----> a or b
# not: Devuelve True si alguno de los operadores es False ----> not a

a = True
b = True
resultado = a and b
print(resultado)

a = True
b = True
resultado = not b
print(resultado)

# Ejercicio(and): Esta en Rango?

valor = int(input('Ingrese el Valor: '))
valormaximo = 5
valorminimo = 0
dentroderango = (valor >= valorminimo) and (valor <= valormaximo)
if dentroderango:
    print(f'{valor} Esta Dentro del Rango')
else:
    print(f'{valor} No Esta Dentro del Rango')

# Ejercicio(or): Puede asistir al juego del hijo?

vacaciones: bool = False
diadedescanso: bool = True
asistencia: bool = (vacaciones or diadedescanso)
if asistencia:
    print(f'Puedo Asistir')
else:
    print(f'No Puedo Asistir')

# Ejercicio(not): Probamos el mismo ejercicio pero con not

vacaciones: bool = False
diadedescanso: bool = True
asistencia: bool = (vacaciones or diadedescanso)
if not asistencia:  # esto es como decir: si no tiene vacacion o dias de descanso, entonces no puede asistir #
    print(f'No Puedo Asistir')
else:
    print(f'Puedo Asistir')

# Ejercicio: Edad entre los 20's o los 30's (usamos and y or)

edad = int(input('ingrese su Edad: '))
veintes: bool = (20 <= edad < 30)
treintas: bool = (30 <= edad < 40)
if veintes:
    print(f'Su Edad Esta Entre los 20\'s')  # la barra inversa "\" muestra que el siguiente caracter no cierra la cadena
elif treintas:  # elif se usa para agregar una segunda condicion
    print(f'Su Edad Esta Entre los 30\'s')
else:
    print(f'Su Edad No Esta Entre los 20\'s o los 30\'s')

# Ejercicio: Cual es el valor mayor? (utilizando una variable tipo bool)

primervalor = int(input('El Primer Valor es: '))
segundovalor = int(input('El Segundo Valor es: '))
esmayor: bool = primervalor > segundovalor
esigual: bool = primervalor == segundovalor
if esmayor:
    print(f'El primer valor ({primervalor}) es mayor a al segundo ({segundovalor})')
elif esigual:
    print(f'{primervalor} es igual a {segundovalor}')
else:
    print(f'El segundo valor ({segundovalor}) es mayor al primero ({primervalor})')

# Ejercicio: Tienda de Libros

print(f'Ingrese los Siguientes Datos del Libro')
nombre = str(input('El Nombre del Libro: '))
idlibro = int(input('ID: '))
precio: float = float(input('Precio: '))
envio = (input('Envio Gratis?(True/False): '))

if envio == 'True':  # es como decir: si escribio true entonces el valor de la variable es true en tipo bool
    envio = True
elif envio == 'False':  # es como decir: si escribio false entonces el valor de la variable es false en tipo bool
    envio = False
else:  # es como decir: si escribio algo que no se true/false entonces el valor de la variable es xx en tipo string
    envio = 'Valor Incorrecto. Ingrese True/False'

# La triple comilla nos permitira imprimir en varias lineas y remplazara el lugar de los inputs se le llamas
# impresion en forma de string
print(f''' 
    Nombre: {nombre}
    ID: {idlibro}
    Precio: {precio}
    Envio gratis: {envio}
''')
