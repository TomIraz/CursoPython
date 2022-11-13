# Debug: ejecucion del programa Paso a Paso

envio = (input('Envio Gratis?(True/False): '))  # este es un punto de ruptura, permitira usar el modo debug

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor Incorrecto. Ingrese True/False'
print(f'''
Envio: {envio}
''')

# Convertir una variable numerica(int, float, etc...) a cadena(str)

numero = int(input('Proporciona un Numero del 1 al 3: '))
numerotexto = ''  # se le asigna el valor de cadena vacia

if numero == 1:
    numerotexto = 'Numero Uno'
elif numero == 2:
    numerotexto = 'Numero Dos'
elif numero == 3:
    numerotexto = 'Numero Tres'
else:
    numerotexto = 'Numero Fuera de Rango'
print(f'''
    Numero: {numerotexto}
''')

# Operador Ternario: se trabaja solo sobre una linea de codigo

condicion = True
print('Condicion Verdadera') if condicion else print('Condicion Falsa')

# Ejercicio: Que estacion es?

mes = int(input('Ingrese Mes: '))
estacion = ''

if 1 <= mes <= 3:
    estacion = 'Es Verano'
elif 4 <= mes <= 6:
    estacion = 'Es Otono'
elif 7 <= mes <= 9:
    estacion = 'Es Invierno'
elif 10 <= mes <= 12:
    estacion = 'Es Primavera'
else:
    print('Valor Incorrecto')

print(f'Para el mes {mes} La estacion {estacion}')

# Ejercicio: Etapa de la vida

edad = int(input('Proporciona tu Edad: '))
etapadevida = ''
if 0 <= edad < 10:
    etapadevida = 'La infancia es increible...'
elif 10 <= edad < 20:
    etapadevida = 'Muchos cambios y mucho estudio...'
elif 20 <= edad <= 30:
    etapadevida = 'Amor y comienza el trabajo'
else:
    etapadevida = 'Etapa de vida no reconocia'
print(f'{etapadevida}')

# Ejercicio: Clasificaciones

nota = float(input('Ingresar Clasificacion (0 a 10): '))
clasificacion = ''

if 0 <= nota < 6:
    clasificacion = 'F'
elif 6 <= nota < 7:
    clasificacion = 'D'
elif 7 <= nota < 8:
    clasificacion = 'C'
elif 8 <= nota < 9:
    clasificacion = 'B'
elif 9 <= nota <= 10:
    clasificacion = 'A'
else:
    clasificacion = 'Valor Desconocido'

print(f'{clasificacion}')
