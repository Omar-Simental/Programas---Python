# Operaciones sobre conjuntos

import os
os.system('clear')
municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}
print(f'El conjunto original        : {municipios}')
print(f'longitud del conjunto       : {len(municipios)}')
print(f'La coleccion es del tipo    : {type(municipios)}')

print('\nLista de municipios usando un ciclo: ')
for m in municipios:
    print(m)

print(f'Esta Zacatecas en conjunto : {"Zacatecas" in municipios}')

print('\nAgrega elementos a un conjunto: ')
municipios.add('Teul')
print(f'Agregar con Add : {municipios}')

otrosmunicipios = {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
municipios.update(otrosmunicipios)
print(f'Agregar con Update : {municipios}')

print('\nEliminar elementos del conjunto: ')
municipios.remove('Zacatecas') # generar error si no existe
print(f'Municipios : {municipios}')

municipios.discard('Ojocaliente') # si no esta no hace nada
print(f'Municipios : {municipios}')

m = municipios.pop() # elimina el tope = el primero
print(m)
print(f'Municipios : {municipios}')

municipios.clear()
print(f'Municipios : {municipios}')