# Numeros romanos a arábigo

numeros = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,'XIX':19,'XX':20 }


print(f'\ndiccionario nuevo : {numeros}')

# imprimir todo el diccionario elemento por elemento
print('\nTodos los elementos del diccionario')
for nr,na in numeros.items():
    print(f'{nr:<12} - {na:5}')

for dl in numeros.items():
    d = int(input('Que dia quieres ? '))
    print (f'El dia que elegiste es : {dl}')