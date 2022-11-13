# Ciclo While: Nos permitira repetir un bloque de codigo
# tantas veces como una condicion sea verdadera
# El ciclo While requiere una condicion de tipo boolean

contador = 0

while contador < 3:
    print(contador)
    contador += 1  # intrementa la misma variable = contador = contador + 1
else:
    print('Fin ciclo while')

# Ejercicio: Imprimir los numeros naturales del 0 al 10

contador = 5

while contador >= 1:
    print(contador)
    contador -= 1
else:
    print('Termino el tiempo')


# Ciclo For: Iterar una lista de datos o una lista de elementos
# Iterar significa recorrer cada elemento, de un conjunto de datos

cadena = 'Hola'  # Las cadenas son Arreglos (conjunto de datos)
# Cada espacio de la cadena esta dividido por indices, la H --> es el indice 0
# la o --> el 1, la l --> 2, la a --> 3

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')

# Ejercicio: Cantitdad de letras a en una palabra

cont = 0
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada {letra}')
        cont += 1
else:
    print(f'La cantidad de a\'s fueron {cont}')
    print('Fin del ciclo')

# Palabra Break: Rompe el ciclo for

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada {letra}')
        break
else:
    print('Fin del ciclo')

# Funcion Range()

for i in range(1,6):  # Definir el rango en el cual trabajaremos, es decir de 0 a 5
    if i % 2 == 0:
        print(f'Valor: {i}')


# Palabra Continue: Se usa para pasar a la siguiente iteracion

for i in range(0,6):
    if i % 2 != 0:
        continue

    print(f'Valor: {i}')
