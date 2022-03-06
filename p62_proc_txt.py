# Procesar texto

txt = '''Aprender a programar en python es una tarea \
que requiere tiempo y constancia, la practica \
es lo que da la experiencia'''

print('\nProcesamiento de la frase: ')
print(f'\n{txt}')
print(f'\nMayusculas : {txt.upper()}')
print(f'\nMinusculas : {txt.lower()}')
print(f'\nTitulo     : {txt.title()}')

pal = 'la'
pos = txt.find(pal)

if pos != -1:
    if txt.startswitch(pal) : print('\nesta al inicio')
    elif txt.endswitch(pal) : print('\nesta al final')
    else:
        print(f'Pos : {pos}')
        print(f'Aparece {txt.count(pal)} veces')
        txt2 = txt.replace(pal, '##')
        print(f'\n{txt2}')
else:
    print(f'\n{pal} no se encuentra la frase')

txt3 = txt.split()
print(f'Seprar : {txt3}')
print(f'Unir : {"-".join(txt3)}')