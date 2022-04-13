# Iterar sobre los elementos de la lista

nums = [2,4,6,8,10,12,14,16]
print(f'Todos los numeros : {nums}')

print('\nIterar con ciclo for : ')
for n in nums:
    print(f'{n:>15} - {n**2:>15} - {n**3:>15}')

print('\niterar con ciclo range : ')
for i in range(len(nums)):
    print(f'{nums[i]} - {nums[i]*10}')

print(f'\nIterar con compresion : ')
[print(n, end='/') for n in nums]