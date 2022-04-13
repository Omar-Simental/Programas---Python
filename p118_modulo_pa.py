# Procesar Poblacion por año

from operator import itemgetter

def imprime(pa, campo, ascdec):
    if campo != '':
        pa = sorted(pa, key=itemgetter(campo), reverse=ascdec)
    print(f"{'Pais':<10} {'2018':>10} {'2019':>10} {'2020':>10} {'2021':>10}")
    for j in pa:
        print(f"{j['Pais']:<10} {j['2018']:>10} {j['2019']:>10} {j['2020']:>10} {j['2021']:>10}")

def valor_mayor(pa, campo):
    m = pa[0][campo]
    jm = [{}]
    for j in pa:
        if j[campo] > m:
            jm[0] = j
    return jm

def valor_menor(pa, campo):
    m = pa[0][campo]
    jm = [{}]
    for j in pa:
        if j[campo] < m:
            jm[0] = j
    return jm

def valor_promedio(pa, campo):
    s = 0
    for j in pa:
        s += j[campo]
    return s / len(pa)