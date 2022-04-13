#Figura de r x c y de un caracter car

def cuadro_caracter(r, c, car):
    print(f'{r} {c} {car}')
    for i in range(1,r+1):
        for j in range(1,c+1):
            print(car, end='')
        print('\r')   


r = int(input('Cuantos renglones    ? '))
c = int(input('Cuantas columnas     ? '))
car = input('Caracter               ? ')

cuadro_caracter(r, c, car)
cuadro_caracter(20, 20, '$')
cuadro_caracter(10,10,'^')