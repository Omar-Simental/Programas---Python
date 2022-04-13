# Calculando el numero menor de tres numeros ingresados por el usuario

def menor(c1, c2, c3):
    if c1<c2 and c1<c3:
        men = c1
    elif c2>c1 and c2>c3:
        men = c2
    elif c3>c1 and c3>c2:
        men = c3
    else:
        men = -1
    return men

print('Dame 3 numeros ?')
a,b,c = float(input()), float(input()), float(input())

m = menor(a,b,c)

if m== -1:
    print('Numeros iguales ')
else:
    print(f'El menor es : {m}')