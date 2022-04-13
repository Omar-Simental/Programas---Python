
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
paga = [100, 200, 300, 400, 500, 600, 700]

while True:
    dia = input('Dame un dia entre lunes y domingo ')
    if dia.lower() in dias:
        break

print(f'Elegiste el dia : {dia} ')
pos = dias.index(dia)
print(f'Corresponde a un paga de: {paga[pos]}')