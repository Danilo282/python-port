"""
Saindo de loop com breaks

Break sai do loop de maneira projetada/forçada

exemplo:

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')


"""
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break

