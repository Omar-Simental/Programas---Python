# Mostrar el dia de la semana segun su numero

print('Mostrando el dia de la semana...')
numero = int(input('Dame un numero... '))
if numero == 1:
    print(f'El dia {numero} es Domingo ')
elif numero == 2:
    print(f'El dia {numero} es Lunes ')
elif numero == 3:
    print(f'El dia {numero} es Martes ')
elif numero == 4:
    print(f'El dia {numero} es miercoles ')
elif numero == 5:
    print(f'El dia {numero} es Jueves ')
elif numero == 6:
    print(f'El dia {numero} es Viernes ')
elif numero == 7:
    print(f'El dia {numero} es Sabado ')
else:
    print('Dia incorrecto')