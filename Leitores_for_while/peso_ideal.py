alt = float(input('Digite sua altura: '))
sexo = input('Digite o sexo - (M/F):  ')

v = sexo
M = (72.7 * alt) - 58
F = (62.1 * alt) - 44.7

if v == M:
    print('Seu peso ideal deve ser: {:.2f}. '.format(M))
else:
    print('Seu peso ideal deve ser: {:.2f}. '.format(F))



