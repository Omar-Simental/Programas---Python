# Contar vocales y consonantes v2

frase = 'El dia se pasa muy rapido'
voc = cons = 0
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c in 'aeiou':
        voc += 1
        print(c, end=' ')
    elif c != ' ' and not c.isdigit():
        cons += 1
print(f'\nVocales = {voc}')
print(f'Consonantes = {cons}')