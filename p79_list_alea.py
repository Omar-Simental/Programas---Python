
import random
l1 = []
l2 = []
l3 = []

c = int(input('Cuantos numeros > '))

print('Generando numeros aleatorios... ')

for n in range(c):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

print('\nListas originales: ')
print(f'Lista 1: {l1}')
print(f'Lista 2: {l2}')

for n in range(c):
    l1[n] = l1[n]**2
    l2[n] = l2[n]**2

for n in range(c):
    l3.append(l1[n] + l2[n])


print('\nListas procesadas: ')
print(f'Lista 1: {l1}')
print(f'Lista 2: {l2}')
print(f'\nLista 3: {l3}')