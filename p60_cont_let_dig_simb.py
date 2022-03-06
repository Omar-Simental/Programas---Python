# Contar letras, digitos, simbolos

frase = input('Dame una palabra ')

car=dig=sim=0
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c.isalpha(): car+=1
    elif c.isdigit(): dig+=1
    else: sim+=1

print(f'Caracteres {car}, Digitos {dig}, Simbolos {sim}')