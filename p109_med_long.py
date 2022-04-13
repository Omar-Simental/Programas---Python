# Conversion de medidas de longitud

def centimetros(long):
    return(long * 2.54)

def metros(long):
    return(long * 3.281)

print('[ 1 ] Convertir a centimetros ')
print('[ 2 ] Convertit a metros ')
op = int(input('elige '))

if op == 1:
    print('Convirtiendo a centimetros ')
    l = int(input('Dame la la longitud en pulgadas '))
    print(f'La longitud en centimetros es : {centimetros(l)}')

if op == 2:
    print('Convirtiendo a metros ')
    l = int(input('Dame la longitud en pies '))
    print(f'La longitud en metros es : {metros(l)}')
