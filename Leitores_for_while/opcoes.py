n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

print('Escolha a opção: ')
print('--------------------------------------------------------------')
print('1 - Soma de 2 numeros ')
print('2 - Diferença entre 2 numeros ( maior pelo menor)  ')
print('3 - Produto entre 2 numeros ')
print('4 - Divisão entre 2 numeros (o denominador não pode ser 0)  ')
print('--------------------------------------------------------------')
op = int(input('Opção: '))

so = n1 + n2
subt = n2 - n1
m = n1 * n2
di = n1 / n2

if op == 1:
    print('O resultado é : {} ' .format(so))
elif op == 2:
    print('O resultado é : {} '.format(subt))
elif op == 3:
    print('O resultado é {} ' .format(m))
elif op == 4:
    print('O resultado é {} ' .format(di))

