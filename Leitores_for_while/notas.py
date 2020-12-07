n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2) / 2
if n1 < 0:
    print('Numero invalido.')
elif n1 >= 10.1:
    print('Numero invalido.')
elif n2 < 0:
    print('Numero invalido.')
elif n2 >= 10.1:
    print('Numero invalido.')
else:
    print('A Media das notas é de : {}. '.format(me))