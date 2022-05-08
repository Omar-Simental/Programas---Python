import pandas as pd

datos = pd.read_csv('edades.csv',header=None, index_col=0).squeeze(1)
datos.name = 'Edades'
print(datos)

# Estadistica descriptiva
print(datos.describe())

# Hacer operaciones especificas sobre la serie

# Suma de todos
print(datos.sum())
# Suma de los primeros tres
print(datos[:3].sum())
# Suma de edades de Angelica, Claudia
print(datos[['Angelica','Claudia']].sum())
# Media de edades de Pedro hasta Sandra
print(datos['Pedro':'Sandra'].sum())
# Desviacion de elementos 11 a 14
print(datos[11:15].mean())
# Sumar 3 a todas las edades
print(datos+3)
# Divide entre 2 todas las edades
print(datos//2)

