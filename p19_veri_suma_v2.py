# Verificar suma v2

print('Verificando si la suma de dos numeros es igual al tercero... ')
print('Dame 3 numero enteros separados por una linea : ')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]
if n1 + n2 == n3:
    print('n1 + n2 = n3')
elif n1 + n3 == n2:
    print('n1 + n3 = n2')
elif n2 + n3 == n1:
    print('n2 + n3 = n1')
else:
    print('No hay sumas que coincidan ')