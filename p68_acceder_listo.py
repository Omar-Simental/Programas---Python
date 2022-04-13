#Acceder a los elementos de una lista

nums = [10,20,30,40,60,70,10,20,99]

print(f'Todos los numeros {nums}')
print(f'Cuantos elementos {len(nums)}')
print(f'Primero y ultimo {nums[0], nums[-1]}')
print(f'Del 2 al 6 {nums[2:6]}')
print(f'Primeros 3 {nums[:3]}')
print(f'Ultimos 3 {nums[6:]}')
print(f'3 antes del ultimo {nums[-4:-1]}')