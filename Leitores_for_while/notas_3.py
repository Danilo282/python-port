n1 = float(input('Digite a nota: '))
p1 = 1
n2 = float(input('Digite a nota: '))
p2 = 1
n3 = float(input('Digite a nota: '))
p3 = 2

mepo = (n1 * p1) + (n2 * p2) + (n3 * p3) / (p1 + p2 + p3)
ap = mepo >= 60
rp = mepo < 60

if mepo >= 60:
    print('Você foi aprovado. Parabens!!!!')
else:
    print('Você foi reprovado!')
print('A Media de suas notas é de: {:.0f}.' .format(mepo))
