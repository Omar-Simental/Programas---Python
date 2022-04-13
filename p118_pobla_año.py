# Procesar Poblacion por año

import p118_modulo_pa as a

pa = [
{'Pais':'Colombia', '2018':49661, '2019':50339, '2020':50883, '2021':51266},
{'Pais':'El Salvador', '2018':6421, '2019':6454, '2020':6486, '2021':6518},
{'Pais':'Mexico', '2018':126191, '2019':127576, '2020':128933, '2021':130262},
{'Pais':'Panama', '2018':4177, '2019':4246, '2020':4315, '2021':4382},
{'Pais':'Uruguay', '2018':3449, '2019':3462, '2020':3474, '2021':3485}
]

# Programa principal
print('\nPor pais de menor a mayor: ')
a.imprime(pa,'Pais', False)
print('\nPor poblacion en 2020 de mayor a menor: ')
a.imprime(pa, '2020', True)

# mayor y menor en 2018
may = a.valor_mayor(pa, '2018')
men = a.valor_menor(pa, '2018')
a.valor_mayor(pa, '2018')
print('\nPais con mayor poblacion del 2018: ')
a.imprime(may,'',False)
print(f'\nPais con menor poblacion en 2018: ')
a.imprime(men,'',False)

# mayor y menor en 2020
may = a.valor_mayor(pa, '2021')
men = a.valor_menor(pa, '2021')
a.valor_mayor(pa, '2021')
print('\nPais con mayor poblacion del 2021: ')
a.imprime(may,'',False)
print(f'\nPais con menor poblacion en 2021: ')
a.imprime(men,'',False)