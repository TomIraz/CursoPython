# Hint: se utilizan los ":" para darle una pista del tipo de variable que sera (bool, int, str, float, etc...)

x: str = 'hola mundo'
print(f'{x}')
print(type(x))

# Sumar variables de tipo int
# input es para procesar entradas del usuario
valor1 = int(input('ingrese valor: '))
valor2 = int(input('ingrese valor: '))
print(valor2 + valor1)


# Concatenar cadenas (str) con "+" o "," la coma agrega un espacio
x: str = "mundo"
print("hola" + x)
# o
x: str = "mundo"
print("hola", x)

# Tipo Bool: Reconocer si la variable es verdadera o falsa
x: bool = 2 > 1
if x:  # es como decir "si x es verdadero imprima verdadero"
    print("es verdadero")
else:
    print("es falso")

# Ejercicio como estuvo tu dia?
midia = input("como estuvo tu dia? (del uno al 10): ")
print(f'mi dia estuvo de {midia}')
