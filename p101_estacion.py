# Dado un numero entre 1 y 4 imprime estacion del a#o con letra

from tkinter import E


def estacion(n):
    if n == 1:
        est = 'Primavera'
    elif n ==2:
        est = 'Verano'
    elif n == 3:
        est = 'Otoño'
    elif e == 4:
        est = 'Invierno'
    else:
        est = 'Error'
    return est

n = int(input('dame un numero entre 1 y 4 '))

e = estacion(n)

if e == 'Error':
    print('Estacion erronea ')
else:
    print(f'La estacion del a#o es: {e}')