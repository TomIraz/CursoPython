# Funciones: Es un bloque de codigo que podemos mandar a llamar n cantidad de veces
# Definir una funcion con 'def'
def miFuncion():
    print('saludos desde mu funcion')


miFuncion()  # Output: saludos desde mi funcion


# Parametros: Son las variables que enviemos con nuestra funcion
# Argumentos: Es el valor que enviemos a nuestra funcion

def miFuncion(nombre, apellido):
    input(print(f'Nombre: {nombre}\nApellido: {apellido}'))


miFuncion('Tomas', 'Irazabal')


# Return: Es para regresar datos de una funcion sin necesidad de guardarlo en una variable
def Sumar(a, b):
    return a + b


print(f'Resultado de la Suma: {(Sumar(2, 4))}')


# Como hacer un Hint en una funcion
def Sumar(a=0, b=0) -> int:  # Hint en funciones: '-> int'
    return a + b


print(f'Resultado de la Suma: {Sumar(2, 8)}')


# Argumentos Variables con * Una Tupla de Valores

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')


# Ejecicio de suma de argumentos variables

def miSuma(*valores):
    resultado = 0
    for valor in valores:
        resultado += valor
    return resultado

print(miSuma(1, 2, 3, 4))


# Ejercicio funcion con argumentos variables para multiplicar los valores

def miMultiplicacion(*args):
    result = 1
    for cuenta in args:
        result = cuenta*result
    return result

print(miMultiplicacion(2, 3, 5))

# Argumentos Variables ** Un Diccionario de Terminos llave-valor

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')

# Distintos tipos de datos como argumentos

def desplegarNombres(nombren):
    for nombre in nombren:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']

desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres(10, 11)  # tirara error
desplegarNombres((2, 3))  # al tomarlo como una tupla entonces funcionara
desplegarNombres([10, 11])  # al tomarlo como una lista entonces funcionara

# Funciones Recursivas
# Factorial

def factorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)  # Usamos la misma funcion en su propia definicion
# lo que hace que sigua el ciclo hasta que sea == a 1 donde no se llama donde termina la recursividad

numero = int(input(f'Su Valor es: '))
resultado = factorial(numero)
print(f'El Factorial de {numero} es: {resultado}')

# Ejercicio Funciones Recursivas: Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas

def Decrease(num):
    if num == 0:
        print(num)
        return num
    else:
        print(num)
        return num - Decrease(num-1)

Decrease(4)

# Ejercicio: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado

def calcular_total(pago_sin_impuestos, impuestos):
    return pago_sin_impuestos + pago_sin_impuestos*(impuestos/100)

pago_sin_impuestos = float(input(f'Ingresar pago: '))
impuestos = float(input(f'Su Impuesto es: '))
print(f'Pago con impuesto: {calcular_total(pago_sin_impuestos, impuestos)}')

# Tarea: Conversion de Temperatura

def C_to_F(cel):
    far = (cel*(9/5)) + 32
    print(far)

def F_to_C(far):
    cel = (far - 32)*(5/9)
    print(cel)

C_to_F(cel=int(input(f'Ingresar Grados Celcius: ')))
F_to_C(far=int(input(f'Ingresar Grados Fahrenheit: ')))
