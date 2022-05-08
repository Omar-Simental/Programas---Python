import pandas as pd

datos = pd.read_csv('edades.csv',header=None, index_col=0).squeeze(1)
datos.name = 'Edades'
print(datos)

# Estadistica descriptiva
print(datos.describe())

# Obtener datos estadisticos especificos

print(  datos.count()   )
print(  datos.mean()   )
print(  datos.std()   )
print(  datos.min()   )
print(  datos.quantile(q=0.25)   )
print(  datos.quantile(q=0.50)   )
print(  datos.quantile(q=0.75)   )
print(  datos.max()   )
print('La moda',  datos.mode()   )