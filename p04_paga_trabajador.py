# Calcula la paga de un trabajador

print('Calculando la paga de un trabajador... ')
nombre = input('Nombre del trabajador ')
horas  = int(input('Horas trabajadas '))
paga   = float(input('Paga por hora ? '))
tasa   = 0.3 

pagabruta = horas * paga
impuesto  = pagabruta * tasa 
paganeta  = pagabruta - impuesto 

print('Resumen de pagos: ')
print(f'El trabajador {nombre} trabajo {horas} horas, con pago de {paga} pesos la hora y una tasa de {tasa} de impuesto ')
print(f'Paga bruta : {pagabruta}')
print(f'Impuesto   : {impuesto}')
print(f'Paga neta  : {paganeta}')