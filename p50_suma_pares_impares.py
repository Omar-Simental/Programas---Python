# Sumar numeros pares y sumar los impares hasta donde el usuario decida

n = int(input('Hasta donde? '))

s = 0
print ('\nNumeros impares...')
for i in range(1,n+1,2):
    print(i,end=' ')
    s += i
print(f'\nSuma de impares: {s}')

s = 0
print ('\nNumeros pares...')
for i in range(2,n+1,2):
    print(i,end=' ')
    s += i
print(f'\nSuma de pares: {s}')