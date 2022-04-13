# Mayor y menor de una lista

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def leerdatos():
    datos = []
    while True:
        d = int(input('numero(-1 termina): '))
        if d == 1: break;
        datos.append(d)
    return datos

nums = [8,7,6.5,6,9.5,7,10,6,7]
nums = leerdatos()
may = mayor(nums)
men = menor(nums)
print(f'El mayor es : {may}')
print(f'El menor es : {men}')