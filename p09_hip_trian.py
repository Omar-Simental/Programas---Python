# Calcular la hipotenusa de un triangulo

import math
print('Calculando la hipotenusa de un triangulo... ')
longlado1  = int(input('Dame el valor de longlado1 '))
longlado2  = int(input('Dame el valor de longlado2 '))
hipotenusa = math.sqrt(longlado1 * longlado1 + longlado2 * longlado2)

print(f'La hipotenusa del triangulo es: {hipotenusa}')
