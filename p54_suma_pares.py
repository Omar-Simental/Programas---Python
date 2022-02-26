# Suma de todos los pares entre 1 y n

n = int(input('Hasta donde? '))

s = 0
print ('\nNumeros pares...')
for i in range(2,n+1,2):
    print(i,end=' ')
    s += i
print(f'\nSuma de pares: {s}')