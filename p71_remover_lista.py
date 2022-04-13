# Remover elementos de la lista

nums = [1,3,5,7,9,11,99,15,88,19,100]
print(f'Todos los numeros       : {nums}')
nums.remove(99)
print(f'Remover 99              : {nums}')
nums.pop(8) 
print(f'Remover [8]             : {nums}')
nums.pop()
print(f'Remover el ultimo : 100 : {nums}')
nums.clear()
print(f'Remover todos           : {nums}')