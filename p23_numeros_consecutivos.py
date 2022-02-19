# Realizar un programa que pida tres numeros consecutivos (3,4,5 o 9,10,11)

print('Revisando si los numeros son consecutivos... ')
print('Dame tres numeros... ')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]
if (n2 == n1 + 1) and (n3 == n2 + 1):
    print(f'Los numeros {n1},{n2},{n3} son consecutivos... Gracias')
else:
    print('Error')