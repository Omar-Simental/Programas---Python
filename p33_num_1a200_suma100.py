# numeros de 1 a 200, hasta sumar 100
# 1 + 2 + 3 + 4 >= 100

c = 0
s = 0
while c < 200:
    c += 1
    s += 1
    print(c,end=' ')
    if s >= 100:
        print('\n')
        break
print(f'Hemos alcanzado la suma {s}')