import pandas as pd

# Leer de un archivo delimitando los datos de de las actividades por estado
datos = pd.read_csv('poblacion.csv', header=None, index_col=0).squeeze(1)
datos.name = 'Poblacion'

# Toda la serie
print('Trabajando con los datos de la serie compreta \n')
print('Orden original', datos, '\n')
print('Orden inverso', datos[::-1], '\n')
print('Orden ascendete por indice ', datos.sort_index(ascending=True), '\n')
print('Orden descendente por indice ', datos.sort_values(ascending=False), '\n')

# Atributos de la serie
print('Los atributos de la serie \n')
print(f'Nombre: {datos.name}, Tamaño: {datos.size}, Tipo: {datos.dtype}, Bytes: {datos.nbytes}, Tamaño de dato: {datos.nbytes / datos.size}')

# Iterar sobre los valores individuales de la serie
print('Iterando sobre los valores individuales de las serie \n')
for m, v in datos.items():
    print(f'La entidad de {m} tiene una poblacion de {v} personas')

# Acceso a datos por indice numerico
print('Ejemplo de acceso a datos por indice numerico \n')
print('Los primeros 5 ', datos[:5], '\n')
print('Los ultimos 5 ', datos[-5:], '\n')
print('Consecutivos ', datos[4:9], '\n')
print('Salteados ', datos[[5,10,15,20]], '\n')

# Acceso a datos por indice alfabetico
print('Ejemplo de acceso a datos por indice alfabetico \n')
print('Los primeros 5 ', datos[:'Coahuila'], '\n')
print('Los ultimos 5 ', datos['Tamaulipas':], '\n')
print('Consecutivos ', datos['Quintana Roo':'Yucatán'], '\n')
print('Salteados ', datos[['Campeche', 'Chiapas', 'Durango','México']], '\n')
print('Los primeros 5 ', datos.head(5), '\n')
print('Los ultimos 5 ', datos.tail(5), '\n')

# Filtrar datos
print('Ejemplo de filtrado de datos en serie \n')
print('Los primeros 5 ', datos.head(5), '\n')
print('Los ultimos 5 ', datos.tail(5), '\n')
print('Valor > 300 ', datos[datos>300].sort_values(ascending=False), '\n')
print('Valores entre 10 y 100 ', datos[(datos>=1) & (datos<=100)].sort_values(), '\n')

# Estadisticas 
print('Estadistica descriptiva de los datos de la serie \n')
print('Resumen estadistico ', datos.describe() )
print(f'Media: {datos.mean()}, Desviacion: {datos.std()}, Minimo: {datos.min()}, Maximo: {datos.max()}')
print(f'Q25: {datos.quantile(q=0.25)} , Q50: {datos.quantile(q=0.50)} , Q75: {datos.quantile(q=0.75)} ')
print('Moda: ', datos.mode())

# Otras operaciones con los datos de la serie
print('Otras operaciones de los datos de la serie \n')
print('La suma de todos         :', datos.sum())
print('La suma primeros 10      :', datos.head(10).sum())
print('La media ultimos 10      :', datos[['Sonora','Zacatecas','Oaxaca']].mean())
print('Incremento del 15%       :', datos*0.15)
print('Sumar 20 a todos         :', datos+20)