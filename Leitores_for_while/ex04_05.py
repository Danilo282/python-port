n1 = int(input('Digite um numero: '))
if n1 >= 0:
    exp = n1 ** 2
    rq = n1 ** (1/2)
    print('O numero digitado foi: {}, e seu quadrado é: {} e sua raiz quadrada é {:.0f}.' .format(n1, exp, rq))
else:
    print('O numero digitado {} é invalido.' .format(n1))