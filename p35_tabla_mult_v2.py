# Tabla de multiplicar 

import os
while(True):
    os.system('cls')
    t = int(input('Cual tabla quieres? '))
    n = int(input('Hasta donde? '))
    c = 1
    while c <= n:
        print(f'{c} x {t} = {c * t}')
        c += 1
    res = input('Deseas otra tabla (S/N) ? ')
    if res.upper() == 'N': break
print('Gracias...')