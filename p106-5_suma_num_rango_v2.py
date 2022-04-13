# Suma numeros en un rango

from re import S


def suma_rango(ini, fin):
    s = 0
    nums = []
    for i in range(ini, fin+1):
        nums.append(i)
        s += i
    return nums, s

print('Dame un rango de valores a sumar ')
ini = int(input('Dame inicio ? '))
fin = int(input('Dame fin ? '))

nums, s = suma_rango(ini, fin)

print(f'Los numero sumados fueron {nums}')
print(f'La suma de los numero fue {s}')