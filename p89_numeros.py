

import os
os.system('clear')
a = {50,60,70,80,90,100,200}
b = {60,90,100,300,400,500}
c = {10,20,60,90,70,100,600,700}
print(f'a : {a}   b : {b}   c : {c}')

#Union
print('\nUnion: ')
d = a.union(b)
print(f'c1 union c2                : {d}')
f = a | c
print(f'c1 union c3                : {f}')
g = set().union(a).union(b).union(c)
print(f'c1 union c2 union c3       : {g}')
d.clear();f.clear();g.clear()

# Diferencia
print('\nDiferencia: ')
d = a.difference(c)
print(f'a: {a} diferencia d: {c} = {d}')
d.clear();

# Diferencia simentrica
print('\nDiferencia simetrica: ')
d = b.symmetric_difference(c)
print(f'b: {b} diferencia simetrica b: {c} = {d}')
d.clear();

# Interseccion
print('\nInterseccion: ')
d = b.intersection(c)
print(f'b: {b} interseccion c: {c} = {d}')
d.clear();

# Subconjunto y Superconjunto 
print('\nsubconjunto o Superconjunto: ')
d = {1,3,5} 
print(f'a: {a} es subconjunto de b: {b}     : {a.issubset(b)} {a<=b}')
print(f'c: {c} es subconjunto de a: {a}     : {c.issubset(a)} {c<=a}')

print(f'100 esta en {a} ?    : {100 in a}')
print(f'60 esta en {a}, {b} y {c} ?    : {60 in a}, {60 in b}, {60 in c}')
print(f'900 no esta en {c} ? : {900 not in c}')