# Verificar si la suma de dos numeros es igual al tercero

print('Verificando si la suma de dos numeros es igual al tercero... ')
print('Dame 3 numero enteros separados por una linea : ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1 + n2 == n3:
    print('Son iguales')
else:
    print('Son distintos')