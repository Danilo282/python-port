x = input('Digite um número positivo maior que 0\n')
if int(x) > 0:
    i = 0
    s = 0
    while i < len(x):
        s = s + int(x[i])
        i = i + 1
    print(f'A soma dos números é: {s}')
else:
    print('Digite Valores Válidos')