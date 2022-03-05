# Secuencia de n renglones v2

r = int(input('Dame un numero '))

for x in range(1,r+1):
    n = 0
    for y in range(1,x+1):
        n += 1
        print(n ,end='')
    print('')  