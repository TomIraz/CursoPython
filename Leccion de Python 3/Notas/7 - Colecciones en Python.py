# LIstas en python: Es un conjunto de elementos
# definimos la lista de nombre
# la lista(variable) en plural y los elementos en singular

nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# imprimimos la lista de nombres
print(nombres)  # output: ['Juan', 'Karla', 'Ricardo', 'Maria']

# acceder a los elementos de una lista
print(nombres[0])  # el primero empezando de la Izquierda
print(nombres[1])

# acceder a los elementos de manera inversa
print(nombres[-1])  # el primero empezando de la Derecha
print(nombres[-2])

# Imprimir un rango de la lista

print(nombres[0:2])  # no se inconye el 2
#  ir desde el inicio de la lista el segundo punto (que no se incluye)
print(nombres[:3])  # output: ['Juan', 'Karla', 'Ricardo']
# ir desde el indice indicado hasta el ultimo indice
print(nombres[1:])  # output: ['Karla', 'Ricardo', 'Maria']


# Iterar una Lista

for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')


# Funcion Len(Lenght): Para saber la cantidad de elementos que tiene una lista
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
print(nombres)
print(len(nombres))

# Funcion append: Para agregar elementos al final de una lista
nombres.append('Lorenzo')
print(nombres)

# Funcion insert: Para agregar elementos en un indicie en específico de una tabla
nombres.insert(2, 'Jose')
print(nombres)

# Funcion remove: Para remover un elemento en una lista
nombres.remove('Karla')
print(nombres)

# Funcion pop: Para remover el último elemento en una lista
nombres.pop()
print(nombres)

# Eliminar un elemento en un índice específico
del nombres[0]
print(nombres)

# Eliminar una lista
del nombres

# Ejercicio: Iterar un rango de 0 a 10 e imprimir solo los numeros divisibles entre 3
for i in range(10):
    if i % 3 == 0:
        print(i)

# Tupla: Es una lista inmutable, respeta el orden, pero son inmodificables
# una tupla de un solo elemento debe contener una como al final si no será una cadena
frutas = ('banana', 'manzana', 'naranja')
print(frutas)
# saber el largo
print(len(frutas))
# acceder a un elemnto
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])  # sin incluir el ultimo indice

# Recorrer los elementos de una tupla

for fruta in frutas:
    print(frutas)

# Evitar el salto de línea por defecto (\n por defecto) esta sin que la veamos

for fruta in frutas:
    print(fruta, end=' ')  # por default sin que lo veamos aparece asi print(frutas, end='\n'), no hay enter

# Modificar una tupla a una lista para modificarla y luego convertirla en una tupla de nuevo

frutaslista = list(frutas)  # creamos la lista frutaslista
# y le asignamos la conversion de la tupla en lista con la funcion "lista(frutas)"
frutaslista[0] = 'Pera'  # modificamos la lista (en el índice 0 agregamos "Pera")
frutas = tuple(frutaslista)  # hacemos lo mismo al revez

# Podemos copiar todos los elementos de una tupla en su orden
tup1 = (13, 1, 8, 3, 2, 5, 8)
lis1 = []
for num in tup1:
    if num < 5:
        lis1.append(num)
print(lis1)

# Set: Es una lista sin orden y sin valores repetidos
# No se pueden modificar los valores almacenados en un set, pero si agregar o eliminar
# El Set se define con llave '{}'

planetas = {'Marte', 'Jupiter', 'Venus'}

# Revisar si un elemento esta presente en un Set

print('marte' in planetas)

# Agregar elementos al Set
planetas.add('Tierra')
print(planetas)

# Eliminar elemento
planetas.remove('Venus')

# Eliminar elementos sin tirar error
planetas.discard('Jupiter')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas


# Diccionario: Tiene una Key y un valor asociado a la llave

diccionario = {
    'IDE': 'Integrated Fevelompent Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

# Largo del diccionario
print(len(diccionario))

# Acceder a un elemento es solo mediante él [key] ente corchetes
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificar elemento
diccionario['IDE'] = 'integrated develompent environment'
print(diccionario)

# Recorrer elemenetos
# Funcion diccionario.items() sirve para mostrar ambos llaves y valores en el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer Keys o llaves
# Funcion diccionario.keys() sirve para mostrar llaves en un diccionario
for llave in diccionario.keys():
    print(llave)

# Recorrer los valores
# Funcion diccionario.values() sirve para mostrar valores en un diccionario
for valor in diccionario.values():
    print(valor)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Elimiar un elemento
diccionario.pop('IDE')
