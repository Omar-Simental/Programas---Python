# Imprime los numeros impares de forma ascendente desde 1 hasta el numero que el usuario decida

c = 1
s = 0
n = int(input('Hasta que numero? '))
while c <= n:
    print(c,end=' ')
    s += c
    c += 2
print(f'\nLa suma es: {s}')