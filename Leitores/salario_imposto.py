sb = float(input('Digite o Salario:R$ '))
s1 = sb * 1.05
s2 = sb * 0.07

sr = s1 - s2
print('O salario a receber é de R${:.2f}'.format(sr))