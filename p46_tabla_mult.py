# Imprime la tabla de multiplicar deseada hasta donde el usuario lo pida

t = int(input('Tabla?  '))
n = int(input('limite? '))
for r in range(1,n + 1):
    print(f'{r} x {t} = {r*t}')