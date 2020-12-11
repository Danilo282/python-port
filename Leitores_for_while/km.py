n1 = int(input('Digite a distancia em Km: '))
n2 = int(input('Digite a quantidade de litros: '))

kml = n1 / n2

if kml < 8:
    print('Venda o carro.')
elif kml > 8 < 14:
    print('Economico.')
elif kml > 14:
    print('Super economico.')