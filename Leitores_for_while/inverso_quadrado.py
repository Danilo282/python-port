n1 = float(input('Digite um numero: '))

if n1 >= 0:
    rq = n1 ** (1/2)
    print("A raiz quadrada de {}, é : {}. ".format(n1, rq))
else:
    nq = n1 ** 2
    print('O numero {} ao quadrado é {}. '.format(n1, nq))