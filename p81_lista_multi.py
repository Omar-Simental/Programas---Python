# Multiplica dos listas para hacer una tercera

c = 5

lista1 = []
print('\nLeyendo los elementos de la lista 1: ')
for i in range(c):
    n = int(input(f'Lista1[{i}] = '))
    lista1.append(n)
print(f'\nLista1 : {lista1}')

lista2 = []
print('\nLeyendo los elementos de la lista 2: ')
for i in range(c):
    n = int(input(f'Lista2[{i}] = '))
    lista2.append(n)
print(f'\nLista2 : {lista2}')

lista3 = []
print('\nCalculando e imprimiendo la suma de las listas ')
for i in range(c):
    lista3.append(lista1[i]*lista2[i])
print(f'\nLista3 : {lista3}')