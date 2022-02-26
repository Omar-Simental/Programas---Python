# Calcula el factorial

n = int(input('Numero? '))

f = 1
for i in range(1,n+1):
    f = f * i
print(f'el factorial es: {f}')