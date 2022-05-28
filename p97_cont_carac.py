# Contar caracteres de una cadena

cadena1 = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
cadena2 = [10,9,8,7.5,6]
valores = dict(zip(cadena1, cadena2))

# imprimir todo el diccionario elemento por elemento
print('\nTodos los elementos del diccionario')
for m,c in valores.items():
    print(f'{m:<12} - {c:5}')