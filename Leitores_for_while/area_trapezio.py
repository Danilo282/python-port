"""
Calcule a area do trapezio

"""

bma = int(input('Digite a base maior: '))
bmen = int(input('Digite base menor: '))
alt = int(input('Digite a altura '))
area = (bma + bmen) * alt / 2

if bma <= 0:
    print('Digite um numero maior que 0.')
elif bmen <= 0 :
    print('Digite um numero maior que 0. ')
else:
    print(' A area do trapézio é de : {}.' .format(area))