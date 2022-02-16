# Numero de la suerte

print('Calculando el numero de la suerte... ')
m, c, d, u = input().split()
m, c, d, u = [int(m), int(c), int(d), int(u)]
suma = (m + c + d + u)

print(f'Dado que naciste en {m},{c},{d},{u} tu numero de la suerte es: {suma}')