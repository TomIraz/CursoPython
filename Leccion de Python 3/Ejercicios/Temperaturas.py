N = int(input('Cantidad de Temperaturas: '))
if N == 0:
    print("0")
else:
    min = None
    for T in map(int, input('Ingresa las Temperaturas: ').split()):
        if (min == None) or (abs(T) < abs(min)) or ((T == -min) and (T > 0)):
            min = T
    print(min)
