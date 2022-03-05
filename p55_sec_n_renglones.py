# Secuencia de n renglones

r = int(input('Dame un numero '))
n = 0
for x in range(1,r+1):
    n += 1
    for y in range(1,x+1):
        print(n ,end='')
    print('')  