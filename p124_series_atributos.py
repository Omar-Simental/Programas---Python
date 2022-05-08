import pandas as pd

datos = pd.read_csv('edades.csv',header=None, index_col=0).squeeze(1)
datos.name = 'Edades'
print(datos)

# Atributos
print(datos.name) # nomber de la serie
print(datos.size) # tipo de datos de los valores de la serie
print(datos.index) # indices de la serie
print(datos.values) # valores de la serie