"""

Menu de operações matematicas

"""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
print('----------------------------------------------------------------------')
print('SELECIONE UMA OPÇÃO ABAIXO: ')
print('')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('-----------------------------------------------------------------------')
r = int(input('Digite a opção para que seja feita a sua operação: '))

soma = n1 + n2
subtrac = n1 - n2
multi = n1 * n2
div = n1 / n2

if r == 1:
    print('O resultado é: {:.0f} '.format(soma))
elif r == 2:
    print('O resultado é: {:.0f}. ' .format(subtrac))
elif r == 3:
    print('O resultado é: {:.0f}. '.format(multi))
elif r == 4:
    print('O resultado é: {:.0f}.' .format(div))