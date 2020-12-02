prod = float(input('Digite o valor do produto: R$  '))
desc = prod * 0.12
vd = prod - desc
print('O valor do produto com o desconto é de: ')
print('----------------------------------------')
print('R${:.2f}'.format(vd))
