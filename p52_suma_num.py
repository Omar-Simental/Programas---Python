# Sumar numeros introducidos por el usuario

n = int(input('Cuantas calificaciones? '))

s = 0
for i in range(1,n+1):
    c = float(input(f'Califiacion {i}? '))
    s += c
print(f'La suma es {s} y el promedio es {s/n}')