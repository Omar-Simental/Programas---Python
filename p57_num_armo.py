# Secuencia de numeros armonicos
# 4 SUMA(4)=1/4+1/3+1/2+1/1 2.083333
#7 SUMA(10)=1/7+1/6+1/5+1/4+1/3+1/2+1/1 2.592857

n = int(input('Numero? '))      # Numero factorial

f = 1
a = 0
for i in range(1,n+1):
    f = f * i
    a += 1 / i
    print(f'para {i} el numero armonico es: {a}')