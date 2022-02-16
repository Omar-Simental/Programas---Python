# Calcular el tiempo por dias, minutos y segundos

print('Calculando el tiempo por dias, minutos y segundos... ')
horas = int(input('Dame las horas transcurridas '))
dias = horas // 24
minutos = horas * 60
segundos = minutos * 60


print(f'Para {horas} horas transcurrieron {dias} dias, {minutos} minutos y {segundos} segundos')