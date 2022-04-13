# Tabla de conversiones

ini = 490
fin = 500



print(f"{'Tabla de Conversiones':^45}")
print('-'*70)
print('{p1:<15}{p2:.^15}{p3:.^15}{p4:>15}'.format(p1='Decimal', p2='Hexadecimal', p3='Octal', p4='Binario'))
print('-'*70)
for i in range(ini,fin+1):
    print('\n{0:d}              {0:x}               {0:o}               {0:b}\n'.format(i))
print('-'*70)