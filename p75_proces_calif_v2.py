# Procesar calificaciones V2

nums = []
n = 0
print('Introduce calificaciones 0..9 (99 para parar)')
while n!=99:
    n = float(input('Dame la calificacion '))
    if n>=0 and n<=10:
        nums.append(n)
    else:
        print('x')
print('<fin')

suma = sum(nums) 
promedio = suma / len(nums)
mp = [n for n in nums if n>promedio]
may = max(nums)
men = min(nums)

print(f'Capturaste {len(nums)} : {nums}')
print(f'\nEstadisticas')
print(f'La suma es : {suma}')
print(f'El promedio : {promedio}')
print(f'Mayores prom : {len(mp)} : {mp}')
print(f'El mayor es : {may}')
print(f'El menor es : {men}')