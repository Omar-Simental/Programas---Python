# Secuencia de numeros armonicos


n = int(input('Numero? '))

f = 1
a = 0
print('Numero\tNA')
print('-' * 15)
for i in range(1,n+1):
    f = f * i
    a += 1 / i
    print(f'{i}\t {a}')
    print('-' * 15)
print(f'El numero armonico de {i} es: {a}')