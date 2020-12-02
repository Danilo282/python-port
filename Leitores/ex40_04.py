hr = 30
desc = 0.08
sol = int(input('Digite a quantidade de dias trabalhados: '))
dia = (sol * hr * 8)
vl1 = (dia * desc)
vlrliq = (dia - vl1)
print('O valor liquido a receber é de R${}'.format(vlrliq))


