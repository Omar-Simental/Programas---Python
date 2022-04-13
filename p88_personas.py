

import os
os.system('clear')
a = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
b = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}
print(f'personas1 : {a}   personas2 : {b}')

#Union
print('\nUnion: ')
c = a.union(b)
print(f'a union b : {c}')
c.clear();

# Interseccion
print('\nInterseccion: ')
c = a.intersection(b)
print(f'a: {a} interseccion b: {b} = {c}')
c.clear();

# Diferencia
print('\nDiferencia: ')
c = a.difference(b)
print(f'a: {a} diferencia b: {b} = {c}')
c.clear();

# Diferencia simentrica
print('\nDiferencia simetrica: ')
c = a.symmetric_difference(b)
print(f'a: {a} diferencia simetrica b: {b} = {c}')
c.clear();

# Subconjunto y Superconjunto 
print('\nsubconjunto o Superconjunto: ')
p3 = {'Pablo', 'Mateo'} 
p4 = {'Reynaldo', 'Angelica'}
print(f'p3: {p3} es subconjunto de c1: {b}     : {p3.issubset(b)} {p3<=b}')
print(f'p4: {a} es superconjunto de c1: {p4}   : {a.issuperset(p4)} {a>=p4}')

print(f'Pedro esta en {a} ?    : {"Pedro" in a}')
print(f'Lilia no esta en {b} ? : {"Lilia" not in b}')