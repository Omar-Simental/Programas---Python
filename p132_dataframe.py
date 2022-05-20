import pandas as pd

nombre      = pd.Series(['Juan','Pedro','Luis','Maria','Genaro','Israel','Fatima','Angelica','Ancelmo'])
edad        = pd.Series([33,35,35,30,25,34,42,22,55])
peso        = pd.Series([45,65.5,30.5,80,45,25,60,45,90])
ojos        = pd.Series(['Cafe','Verde','Azul','Negro','Cafe','Verde','Azul','Violeta','Negro'])
estatura    = pd.Series([1.22,1.70,1.80,1.66,1.50,1.90,1.33,1.75,1.80])
promedio    = pd.Series([8.5,7.0,6.5,10,9.5,5,8,7.5,5])
municipio   = pd.Series(['Jerez','Fresnillo','Rio Grande','Panfilo Natera','Zacatecas','Jerez','Fresnillo','Panfilo Natera','Fresnillo'])

# Crear un DataFrame en base a Series
df = pd.DataFrame(data={"Nombre": nombre, "Edad": edad, "Peso": peso, "Ojos": ojos, "Estatura": estatura, "Promedio": promedio, "Municipio": municipio})
df.set_index('Nombre', inplace = True)
print(df)

# Atributos
print('Informacion del DataFrame    :\n', df.info(), '\n')
print('Indices del DataFrame        :\n', df.index, '\n')
print('Valores del DataFrame        :\n', df.values, '\n')
print('Columnas del DataFrame       :\n', df.columns, '\n')
print('Tipos de datos del DataFrame :\n', df.dtypes, '\n')
print('Forma del DataFrame          :\n', df.shape, '\n')
print('Tamaño del DataFrame         :\n', df.size, '\n')
print('Dimensiones del dataFrame ?  :\n', df.ndim, '\n')
print('La serie esta vacia ?        :\n', df.empty, '\n')
print('Uso de la memoria            :\n', df.memory_usage(), '\n')

# Iterar por los elementos del DataFrame
print('\nIterar por los renglones de DataFrame en base al par (columna,serie)\n')
for columna, serie in df.items():
    print('\nColumna: ', columna, '\n')
    print('Serie: \n', serie)

# Iterar por los renglones del DataFrame
print('\nIterar por los renglones del DataFrame en vase al par (indice,Columna)\n')
for indice, columna in df.iterrows():
    print(indice, 'tiene', columna['Edad'],'años de edad')

for indice, columna in df.iterrows():
    print(indice, 'pesa', columna['Peso'],'Kg')

print('\nIterr por renglones en base tuplas\n')
for ren in df.itertuples(index='Nombre'):
    print(ren)

# Acceder a una serie y suys elementos
print('\nAcceder a una Serie completa por su indice alfabetico\n')
print(df['Edad'], '\n')
print('\nAcceder a una Serie completa por su nombre\n')
print(df.Edad, '\n')
print('\nAcceder a los elementos tope o la cola del DataFrame\n')
print(df.head(3), '\n')
print(df.tail(3), '\n')

print('\nAcceder a los elementos tope o la cola de una serie especifica:\n')
print(df['Promedio'].head(3), '\n')
print(df.Ojos.tail(3), '\n')

# Acceder a los renglones con iloc
print('\nAcceder a un renglon especifico con iloc \n')
print(df.iloc[0])
print('\nAcceder a renglones continuos con iloc \n')
print(df.iloc[1:4])
print('\nAcceder a renglones dispersos con iloc \n')
print(df.iloc[[1,3,5]])
print('\nAcceder a renglones alternados (uno si y uno no) con iloc \n')
print(df.iloc[0:10:2])

# Acceder a las columnas con iloc
print('Acceder a un columnma con iloc')
print( df.iloc[:,0])
print('Acceder columnmas consecutivas con iloc')
print( df.iloc[:,0:3])
print('Acceder columnmas dispersas con iloc')
print( df.iloc[:,[0,3]])
print('Acceder columnmas alternadas con iloc')
print( df.iloc[:,0:6:2])

# Acceder a los renglones con loc
print('\nAcceder a un renglon especifico con loc \n')
print(df.loc['Juan'])
print('\nAcceder a renglones continuos con loc \n')
print(df.loc['Maria':'Fatima'])
print('\nAcceder a renglones dispersos con loc \n')
print(df.loc[['Juan','Genaro','Ancelmo']])
print('\nAcceder a renglones alternados (uno si y uno no) con loc \n')
print(df.loc['Juan':'Ancelmo':2])

# Acceder a las columnas coniloc
print('Acceder a un columnma con loc')
print( df.loc[:,'Edad'])
print('Acceder columnmas consecutivas con loc')
print( df.loc[:,'Edad':'Ojos'])
print('Acceder columnmas dispersas con loc')
print( df.loc[:,['Edad','Ojos','Promedio']])
print('Acceder columnmas alternadas con loc')
print( df.loc[:,'Edad':'Municipio':2])

# Acceder elemento especifico del DataFrame con iat y at
print('\nAcceder a elementos especificos del DataFrame con iat \n')
print(df)
print('\nEl primer renglon y primera columna (Edad de Juan)    :' , df.iat[0,0] )
print('\nEl ultimo renglon y ultima columna (Municipio de Ancelmo)    :' , df.iat[8,5] )

print('\nAcceder a elementos especificos del DataFrame con at \n')
print('\nEl primer renglon y primera columna (Edad de Juan)    :' , df.at['Juan','Edad'] )
print('\nEl ultimo renglon y ultima columna (Municipio de Ancelmo)    :' , df.at['Ancelmo','Municipio'] )

# Filtrar datos en el DataFrame directamente
print('\nFiltrar por un cierto ejemplo 1 \n')
print(df[ df['Edad'] > 30])
print('\nFiltrar por un cierto ejemplo 2 \n')
print(df[ df.Municipio.isin(['Fresnillo','Jerez']) ])
print('\nFiltrar por un cierto ejemplo 3 \n')
print(df[ df['Ojos'].str.startswith('V') ])
print('\nFiltrar en base a dos criterios \n')
print(df[ (df['Edad'] > 30) & (df['Ojos']=='Verde')])

# Filtrar datos en el DataSetcon query
print('\nFiltrar por un criterio ejemplo 1\n')
print(df.query('Edad > 30') )
print('\nFiltrar por un criterio ejemplo 2\n')
print(df.query("Ojos != 'Verde'") )
print('\nFiltrar por un criterio ejemplo 3\n')
print(df.query("Municipio in ('Zacatecas','Panfilo Natera')") )
print('\nFiltrar por dos criterios a la vez ejemplo 1\n')
print(df.query("Edad > 30 & Ojos == 'Verde' ") )
print('\nFiltrar por dos criterios a la vez ejemplo 2\n')
print(df.query("Estatura >= 1.70 & Estatura <= 1.80 ") )
print('\nFiltrar por dos criterios a la vez ejemplo 3\n')
print(df.query("Municipio not in ('Fresnillo','Panfilo Natera') & Edad <= 25 "))

# Estadisticas con el DataFrame
print('\nEstadistica descriptiva del DataFrame: \n')
print(df.describe())
print('\nEstadistica descriptiva individual: \n')
print('La cuenta        :\n', df.count(), '\n')
print('La media         :\n', df.mean(numeric_only=True), '\n')
print('La Desviacion    :\n', df.std(numeric_only=True), '\n')
print('El minimo        :\n', df.min(numeric_only=True), '\n')
print('El maximo        :\n', df.max(numeric_only=True), '\n')
print('El Q25           :\n', df.quantile(q=0.25), '\n')

print('\nEstadistica descriptiva de una serie: \n')
print(df['Edad'].describe(), '\n')
print(df.Estatura.describe(), '\n')

# Operaciones sobre el DataFrame
print('\nLa suma del DataFrame: \n')
print(df.sum(numeric_only=True))
print('\nLa suma de la serie especifica del DataFrame: \n')
print('La suma del peso     :', df.Peso.sum())
print('La suma de la edad   :', df['Edad'].sum())
print(df['Edad'].mean(), '\n')
print(df['Edad'].sum(), '\n')

print('\nLa desviacion estandar de datos especificos del DataFrame: \n')
print('\nLa desviacion de los primeros 5 ')
print(df.head().std(numeric_only=True))
print('\nLa desviacion de Juan hasta Gnraro')
print(df.loc['Juan':'Genaro'].std(numeric_only=True))
print('\nLa desviacion de Estatura y Promedio')
print(df.loc[:,['Estatura','Promedio']].std(numeric_only=True))

# Operaciones sobre el DataFrame agrupar
print('\n Agrupar datos \n')
print('\n Agrupar por una columna: ')
print(df.groupby('Ojos').sum())
print('\n Agrupar por una columna: ')
print(df.groupby('Ojos').mean())
print('\n Agrupar por dos columnas: ')
print(df.groupby(['Municipio','Ojos']).mean())

# Otras operaciones sobre el DataFrame con eval
print('\nOperaciones con el DataFrame con eval')
print('\nSuma de edad y Peso')
print(df.eval('Suma = (Edad + Peso) - Estatura'))
print('\nCon peso > 70, expresion Boleana')
print(df.eval('Peso>70'))
print('\nCon peso mayor al peso promedio', df.Peso.mean())
print(df.eval('Peso >= Peso.mean()'))