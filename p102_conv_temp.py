# Conversion de temperaturas

def farenheit(temp):
    return ( temp * 9/5 ) + 32

def centigrados(temp):
    return ( temp - 32 ) * 5/9 


print('[ 1 ] Convertir a Farenheit ')
print('[ 2 ] Convertir a Centigrados ')
op = int(input('Elige '))

if op == 1:
    print('Convirtiendo a Farenheit ')
    t = int(input('Dame la temperatura en grados Centrigrados '))
    print(f'La temperatura en grados Farenheit es {farenheit(t)}')

elif op == 2:
    print('Convirtiendo a Centigrados ')
    t = int(input('Dame la temperatura en grados Farenheit '))
    print(f'La temperatura en grados Farenheit es {centigrados(t)}')