# Imprime hasta la tabla de multiplicar deseada y hasta donde el usuario lo pida

t = int(input('Hasta que tabla?  '))
n = int(input('limite? '))

for x in range(1,t+1):
    print('-'*10)
    for r in range(1,n + 1):
        print(f'{x} x {r} = {r*x}')
    print('-'*10)