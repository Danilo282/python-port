hrtb = int(input('Digite valor hora de trabalho: R$ '))
hrm = int(input('Digite a quantidade de horas trabalhadas no mês: '))
s1 = (hrtb * hrm) * 1.10
print('O valor a ser pago ao funcionario é de R${:.2f}'.format(s1))