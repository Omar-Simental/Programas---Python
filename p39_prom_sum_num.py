# Calcular el promedio y la suma de numeros introducidos por el usuario

c = s = prom = 0
while True:
    n = int(input('Numero? '))
    if n == 0: break
    s += n
    c += 1
    prom = s/c
print(f'Se introdujeron {c}')
print(f'La suma de los numero es {s}')
print(f'El promedio de los numeros es: {prom}')