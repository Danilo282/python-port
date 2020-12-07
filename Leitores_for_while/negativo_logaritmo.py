import math
n1 = int(input('Digite um numero: '))
x = math.log(n1)

if n1 < 0:
    print('Numero invalido, digite outro valor.')
else:
    print('O logaritmo do numero digitado é {}. '.format(x))