# Secuencia de n renglones

r = int(input('Cuantos renglones? '))
c = input('Caracter? ')

for x in range(1,r+1):
    for y in range(1,x+1):
        print(c,end='')
    print('')  