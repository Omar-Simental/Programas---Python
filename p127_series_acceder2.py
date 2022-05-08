import pandas as pd

datos = pd.read_csv('edades.csv',header=None, index_col=0).squeeze(1)
datos.name = 'Edades'
print(datos)
# Acceder a los datos de una serie en base a su indice alfabetico

# Edad de Santiago
print(datos['Santiago'])
# Los tres primeros datos
print(datos[:'Antonio'])
# Los tres ultimos datos
print(datos['Claudia':])
# Elementos concecutivos Monica hasta Angelica
print(datos['Monica':'Angelica'])
# Elementos no concecutivos Carlos, Esteban, Monica
print(datos['Carlos','Esteban','Monica'])