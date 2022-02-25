# Tabla de multiplicar 

while(True):
    t = int(input('Cual tabla quieres? '))
    c = 1
    while c <= 10:
        print(f'{c} x {t} = {c * t}')
        c += 1
    res = input('Deseas otra tabla (S/N) ? ')
    if res.upper() == 'N': break
print('Gracias...')