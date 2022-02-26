# Calcular temperatura de grados centigrados a grados farenheit de un rando de valores introducido por el usuario

ti = float(input('Temperatura inicial... '))
tf = float(input('Temperatura final... '))
c = ti
print('°C\t°F')
print('-' * 15)
while c <= tf:
    print(f'{c}\t{(c * 9/5) + 32:.2f}')
    c += 1
print('-' * 15)