# Calcular el volumen de un cilindro

import math
print('Calculando el volumen de un cilindro... ')
radio = float(input('Dame el radio del cilindro '))
altura = float(input('Dame la altura del cilindro '))
volumen = math.pi * (radio*radio) * altura

print(f'Para un cilindro de radio: {radio} y altura {altura} su volumen es: {volumen}')