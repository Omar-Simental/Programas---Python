
nombres = []
edades = []
print('Introduce los nombres y edades: * en nombre termina\n')

while True:
    nombre = input('Nombre: ')
    if nombre == '*':
        break
    else:
        nombres.append(nombre)
        edad = int(input('Edad: '))
        edades.append(edad)
print(f'Nombres : {nombres}')
print(f'Edades  : {edades}')

print(f'\nAlumnos mayores de edad')
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f'Nombre: {nombres[i]}, Edad: {edades[i]}')

may = max(edades)
pos = edades.index(may)

print(f'Alumnmo de mayor edad: {nombres[pos]}, {edades[pos]}')