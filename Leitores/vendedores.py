vt = int(input('Digite o valor do produto: R$ '))
tp = (vt * 0.10)
vf = (vt - tp)
print('--------------------------------------------------------')
print('O valor total pago com desconto é de R${:.2f}'.format(vf))
print('--------------------------------------------------------')
vparc = (vt / 3)
print('O valor parcelado sem juros é de R${:.2f}'.format(vparc))
print('--------------------------------------------------------')
cmvd = vf * 0.05
print('A comissão na venda a vista é de R${:.2f}'.format(cmvd))
print('--------------------------------------------------------')
cmvdp = vt * 0.05
print('A comissão na venda a prazo é de R${:.2f}'.format(cmvdp))
