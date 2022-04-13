# Dado un numero entre 1 y 7 imprime el dia de la semana

from tkinter import E


def dia_semana(n):
    if n == 1:
        ds = 'Lunes'
    elif n == 2:
        ds = 'Martes'
    elif n == 3:
        ds = 'Miercoles'
    elif n == 4:
        ds = 'Jueves'
    elif n == 5:
        ds = 'Viernes'
    elif n == 6:
        ds = 'Sabado'
    elif n == 7:
        ds = 'domingo'
    else:
        ds = 'Error'
    return ds

n = int(input('dame un numero entre 1 y 7: '))

e = dia_semana(n)

if e == 'Error':
    print('Dia erroneo ')
else:
    print(f'El dia es: {e}')