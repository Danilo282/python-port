s1 = float(input('Digite o salario: R$ '))
vp = float(input('Digite o valor da prestação: R$ '))
s20 = s1 * 0.20

if vp > s20:
    print('Emprestimo não concedido. Valor superior a 20% do salario.')
else:
    print('Emprestimo concedido.')