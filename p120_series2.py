import pandas as pd

a = [1,7,2,4,8,16,77,45.5]

miserie = pd.Series(a, index = ['a','b','c','d','e','f','g','h'])

print(miserie)

print(miserie[0])
print(miserie[7])
print('\n')
print(miserie['a'])
print(miserie['h'])