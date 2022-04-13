# Promedio y mayores que el promedio

"""
Calcula el promedio de los elementos en una lista
Recibe una liste y regresa un numero entero
"""
def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

"""
Calcula cuales elementos de una lista son mayores al promedio
Recibe una lista y regresa una lista con los mayores al promedio
"""

def mayoresprom(lista, prom):
    mp = []
    for n in lista:
        if n > prom:
            mp.append(n)
    return mp

"""
Leer numeros flotantes hasta introducir -1
Regresa la lista de numeros introducidos
"""

def leerdatos():
    datos = []
    while True:
        d = float(input('numero(-1 termina): '))
        if d == -1: break;
        datos.append(d)
    return datos



#nums = [9,8,7.5,6,9.5,7,10,6,7]
nums = leerdatos()
prom = promedio(nums)
mp = mayoresprom(nums, prom)
print(f'Los numeros son : {nums} - {len(nums)}')
print(f'El promedio es : {prom}')
print(f'Mayores al promedio : {mp} - {len(mp)}')