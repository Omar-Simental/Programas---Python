# Pares e impares en una lista

from re import S


def pares_impares(nums):
    pares = []
    impares = []
    for n in nums:
        if n % 2 == 0 : pares.append(n)
        else: impares.append(n)
    return pares, impares


def sumatodos(l1, l2):
    s = 0
    for n in l1:
        s = s + n**2
    for n in l2:
        s = s + n**2
    return s


nums = [9,8,7.5,6,9.5,7,10,6,7]

pares, impares = pares_impares(nums)

print(f'Los numeros son : {nums} - {len(nums)}')
print(f'Los pares son : {pares} - {len(pares)}')
print(f'Los impares son : {impares} - {len(impares)}')

print(f'La suma de todos elevados al cuadrado es {sumatodos(pares,impares)}')