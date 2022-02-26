# Calcular la suma de numeros introducidos por el usuario hasta llegar a 200

lim = 0         #limite a contar
ni  = 0
s   = 0
while lim < 200:
    c = int(input('Numero? '))
    lim += c
    ni += 1
    s += lim
    print(lim,end=' ')
print(f'\nSe introdujeron {ni} numeros')
print(f'\nHemos alcanzado la suma {lim}')
print(f'La suma de los numeros introducidos es {s}')