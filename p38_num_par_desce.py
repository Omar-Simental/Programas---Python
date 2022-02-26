# Imprime numeros pares de forma descendente desde 100 hasta donde el usuario pida

c = 100
s = 0
n = int(input('Hasta que numero? '))
while c >= n:
    print(c,end=' ')
    s += c
    c -= 2
print(f'\nLa suma es: {s}')