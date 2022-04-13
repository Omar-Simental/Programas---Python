# Suma numeros pares o impares en un rango

from re import S

def suma_pares_impares(ini, fin):
    sp = 0
    si = 0
    pares = []
    impares = []
    for i in range(ini, fin+1):
        if i % 2 == 0 : 
            pares.append(i)
            sp += i
        else: 
            impares.append(i)
            si += i
    return pares, impares, sp, si


print('[ 1 ] Numeros pares ')
print('[ 2 ] Numeros impares ')
op = int(input('elige '))

print('Dame un rango de valores a sumar ')
ini = int(input('Dame inicio ? '))
fin = int(input('Dame fin ? '))

pares, impares, sp, si = suma_pares_impares(ini, fin)

if op == 1:
    print('Sumando numeros pares ')
    print(f'Los numeros pares sumados fueron {pares}')
    print(f'La suma de los numero fue {sp}')

if op == 2:
    print('Sumando numeros impares ')
    print(f'Los numeros impares sumados fueron {impares}')
    print(f'La suma de los numero fue {si}')