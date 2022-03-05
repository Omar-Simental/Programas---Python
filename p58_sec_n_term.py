# Secuencia de n terminos

r = int(input('Cuantos terminos '))
n = 1
o = 0
s = 0
for x in range(1,r+1):
    o += n 
    n *= 10
    s += o
    print(f'{o} ',end=' ')  
print(f'\nLa suma es: {s}')