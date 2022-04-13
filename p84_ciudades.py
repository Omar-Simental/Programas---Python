# Lista de ciudades

nombres_ciudades = []
edades = []
c = 0
print('Introduce los nombres y edades: * en nombre termina\n')

while True:
    nombre = input('Nombre: ')
    if nombre == '$':
        break
    else:
        c += 1
        nombres_ciudades.append(nombre)
print(f'Son : {c} Ciudades')
print(f'Nombres : {nombres_ciudades}')

desc = nombres_ciudades.sort()
print(f'Nombres en orden descendente: {nombres_ciudades}')

