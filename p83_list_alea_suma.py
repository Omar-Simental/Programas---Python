

import random
l1 = []
l2 = []
l3 = []
l4 = []

c = 10
print('Generando numeros aleatorios... ')

for n in range(c):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

for n in range(c):
    l3.append(l1[n] + l2[n])

for n in range (c):
    if l1[n] % 2 != 0 and l2[n] % 2 != 0:
        l4.append(l1[n] + l2[n])


print(f'Lista 1: {l1}')
print(f'Lista 2: {l2}')
print(f'\nLa suma de las listas es: Lista 3: {l3}')
print(f'\nLa suma de los impares es : Lista 4: {l4}')