# Contar vocales y consonantes

frase = input('Dame un frase ')
voc = cons = 0
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c in 'aeiou':
        voc += 1
    elif c != ' ' and not c.isdigit():
        cons += 1
print(f'Vocales = {voc}')
print(f'Consonantes = {cons}')