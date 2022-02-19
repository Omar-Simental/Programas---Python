# Calcular el mayor de tres numeros

print('Calculando el mayor de tres numeros...')
print('Dame tres numeros... ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1 > n2 and n1 > n3:
    print(f'El numero mayor es {n1}')
elif n2 > n1 and n2 > n3:
    print(f'El numero mayor es {n2}')
elif n3 > n1 and n3 > n2:
    print(f'El numero mayor es {n3}')
else:
    print('Los numeros son iguales')