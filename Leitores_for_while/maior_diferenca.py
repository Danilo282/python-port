n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro numero é maior.')
elif n2 > n1:
    print('O segundo numero é maior. ')

n3 = n1 - n2

print('A diferença entre os numeros digitados é de : {:.0f} '.format(n3))