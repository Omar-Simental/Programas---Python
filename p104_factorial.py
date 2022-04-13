#Calcular factorial

def factorial(numero):
    f = 1
    for n in range(1,numero+1):
        f = f * n
    return f

num = int(input('Dame un numero ? '))
print(f'El factorial de {num} es {factorial(num)}')