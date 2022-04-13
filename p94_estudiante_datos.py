# Estudiantes y sus datos

grupo = [
{'nombre':'Omar','edad':24,'carrera':'IRM', 'promedio':9},
{'nombre':'Ariana','edad':23,'carrera':'Lilex', 'promedio':10}
]
print(f'Grupo original {grupo}')

n = int(input('Cuantos estudiantes deseas procesar ? '))

datos = {}

for i in range(n):
    print(f'Estudiante {i+1}')
    nombre = input('Nombre ? ')
    edad = int(input('Edad? '))
    carrera = input('Carrera? ')
    promedio = float(input('Promedio? '))
    datos['nombre'] = nombre 
    datos['edad'] = edad 
    datos['carrera'] = carrera 
    datos['promedio'] = promedio 
    print(f' - Se creo diccionario {datos}')
    grupo.append(datos)

print(f'Grupo completo: {grupo}')
print(f'\nLos nombre de los estudiantes en el grupo : \n')
for e in grupo:
    for k,v in e.items():
        print(f'{k} : {v}')
