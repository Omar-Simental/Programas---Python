# Segunda ley de newton (fuerza = masa * aceleracion)

print('Calculando los valores de la segunda ley de newton... ')
print('Calcular la fuerza........ [f] ')
print('Calcular la masa.......... [m] ')
print('Calcular la aceleracion... [a] ')
op = str.lower(input('Elige una opcion '))
if op == 'f':
    print('\nCalculando la fuerza... ')
    m = float(input('Dame la masa '))
    a = float(input('Dame la aceleracion '))
    f = m * a
    print(f'\nLa fuerza es {f} ')
elif op == 'm':
    print('\nCalculando la masa... ')
    f = float(input('Dame la fuerza '))
    a = float(input('Dame la aceleracion '))
    m = f / a
    print(f'\nLa masa es {m} ')
elif op == 'a':
    print('\nCalculando la aceleracion... ')
    f = float(input('Dame la fuerza '))
    m = float(input('Dame la masa '))
    a = f / m
    print(f'\nLa masa es {a} ')
else:
    print('\nElegiste una opcion invalida... ')
print('\nPrograma terminado, muchas gracias... ')