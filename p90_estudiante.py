# Estudiante en un diccionario

estudiante = {
'nombre':'Omar', 
'edad':24,
'email':'33145571@uaz.edu.mx',
'carrera':'IRM'
}

print(f'\nEl diccionario: {estudiante}')

print('\nLas llaves: ')
for k in estudiante.keys():
    print(k)

print('\nLos valores: ')
for v in estudiante.values():
    print(v)

print('\nLlaves y valores: ')
for k,v in estudiante.items():
    print(f'{k:<10} : {v}')