# Numero mayor de 3 numeros

def mayor(c1, c2, c3):
    if c1>c2 and c1>c3:
        may = c1
    elif c2>c1 and c2>c3:
        may = c2
    elif c3>c1 and c3>c2:
        may = c3
    else:
        may = -1
    return may

print('Dame 3 numeros ?')
a,b,c = float(input()), float(input()), float(input())

m = mayor(a,b,c)

if m== -1:
    print('Numeros iguales ')
else:
    print(f'El mayor es : {m}')