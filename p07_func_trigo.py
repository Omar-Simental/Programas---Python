# Calcular funciones trigonometricas 

import math
print('Calculando funciones trigonometricas')
angulograd   = int(input('Dame el angulo en grados '))
angulo       = math.radians(angulograd)
seno         = math.sin(angulo)
coseno       = math.cos(angulo)
tangente     = math.tan(angulo)
print(f'seno {seno}, coseno {coseno}, tangente {tangente}')