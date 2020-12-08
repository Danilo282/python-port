a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

print('Mostrando o tipo de triangulo: ')
print('')
print('----------------------------------------------------')

if a != b != c or c != a or c != b or b != a:
    print('Triangulo Escaleno')
elif a == b == c:
    print('Triangulo Equilatero')
elif a == b or a == c or b == c:
    print('Triangulo Isosceles')
