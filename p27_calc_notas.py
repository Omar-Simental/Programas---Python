# Calcular el promedio de cinco calificaciones

print('Calculando el promedio de cinco calificaciones... ')
print('Dame tus cinco calificaciones... ')
n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()) ,int(input())
suma = n1 + n2 + n3 + n4 + n5
promedio = suma / 5
if promedio <= 6:
    print(f'Tu promedio es de {promedio} Quedas reprobado')
elif promedio > 6 and promedio <= 7:
    print(f'Tu promedio es de {promedio} Pasas de panzazo')
elif promedio > 7 and promedio <= 8:
    print(f'Tu promedio es de {promedio} Muy bien pues mejorar')
elif promedio > 8 and promedio <= 9:
    print(f'Tu promedio es de {promedio} Excelente sigue asi')
elif promedio > 9 and promedio <= 10:
    print(f'Tu promedio es de {promedio} Perfecto tu esfuerzo valio la pena')
else: 
    print('Error')