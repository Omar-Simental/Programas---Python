# Aceptar estudiantes mayores de 21 años con calificaciones entre 8 y 9.5

print('Evaluando estudiantes mayores de 21 años con calificaciones entre 8 y 9.5  ')
nombre = input('Dame tu nombre ')
edad = int(input('Dame tu edad '))
if edad  >= 21:
    print('Dame tres calificaciones... ')
    n1, n2, n3 = int(input()), int(input()), int(input())
    suma = n1 + n2 + n3
    promedio = suma / 3
    if promedio >= 8 and promedio <= 9.5:
        print(f'{nombre} Bienvenido, edad {edad}, promedio {promedio}')
    else:
        print('Solo aceptamos calificaciones entre 8 y 9.5 ')
else:
    print('Solo aceptamos a mayores de 21 años')