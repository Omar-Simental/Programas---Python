# numeros de 1 a 200 de 10 en 10

c = 1
n = int(input('Hasta donde quieres contar...? '))
while c <= n:
    c += 1
    if c % 10 != 0:
        continue
    print(c, end=' ')