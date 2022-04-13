# Imprimiendo dia del mes y nombre del mes

dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
diasf =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
mes = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

while True:
    m = input('Dame un mes en numero ')
    if dias.lower() in dias:
        break

print(f'Elegiste el dia : {dias} ')
pos = dias.index(dias)
print(f'Corresponde a un paga de: {[pos]}')