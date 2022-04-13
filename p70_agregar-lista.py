# Agregar elementos a la lista

nums = [80.3,12.5,60.2,30.4]
print(f'Todos los numeros           : {nums}')
nums.append(90)
nums.append(100)
print(f'Agregar 90 y 100 al final   : {nums}')
nums.insert(4,80)
print(f'Insertar 80 en [4]          : {nums}')
otros = [110,120,130]
nums.extend(otros)
print(f'Extender con 110,120,130    : {nums}')
n = int(input('Numero > '))
nums.append(n)
print(nums)