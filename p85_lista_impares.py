# Calcular la suma y el promedio de una lista de numeros impares

c = int(input('Cuantos elementos ? '))

lista1 = []
listade3 = []

print('\nLeyendo los elementos de la lista 1: ')
for i in range(c):
    n = int(input(f'Lista1[{i}] = '))
    if n % 2 != 0:
        lista1.append(n)
        if n % 3 == 0:
            listade3.append(n)
print(f'\nLista1 : {lista1}')
print(f'\nListade3 : {listade3}')


suma = sum(lista1) 
sumade3 = sum(listade3)
promedio = suma / len(lista1)

ni = int(input('Que elemento buscas ? '))
pos = lista1.index(ni)

print(f'La suma es : {suma}')
print(f'El promedio : {promedio}')
print(f'La suma de los numeros divisibles entre 3 es : {sumade3}')
print(f'La posicion del elemento {ni} es: {pos}')
