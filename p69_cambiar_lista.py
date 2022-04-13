# Cambiar los elementos de una lista

nums = [10,9,8.5,6.5,9.8,7,5,6.2,9.5]

print(f'Todos                       : {nums}')
nums[0] = 7
nums[1] = 7
print(f'[0] y [1] ponerlos en 7     : {nums}')
nums[2:5] = [9,9,9]
print(f'[2:5] ponerlos en 9,9,9     : {nums}')
nums[5:1] = [10,10,10]
print(f'[5:1] ponerlos en 10,10,10  : {nums}')
nums[8:12] = [8]
print(f'[8:12] ponerlos en 8        : {nums}')