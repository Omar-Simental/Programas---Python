# Aceptar estudiantes mayores de edad con calificaciones mayores o iguales a 8

print('Evaluando estudiantes mayores de edad con calificaciones mayores o iguales a 8 ')
nombre = input('Dame tu nombre ')
edad = int(input('Dame tu edad '))
if edad  >= 18:
    print('Dame dos calificaciones: ')
    c1, c2 = input().split()
    c1, c2 = [int(c1), int(c2)]
    if c1 >= 8 and c2 >= 8:
        print(f'{nombre} Bienvenido, edad {edad}, calificaciones {c1}, {c2}')
    else:
        print('Solo aceptamos calificaciones mayores a 8 ')
else:
    print('Solo aceptamos a mayores de edad')