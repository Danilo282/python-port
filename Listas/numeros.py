lista = list(range(21))
lista2 = list('Danilo')
print(lista)
print(lista.count(10))

num = int(input('Digite um numero: '))
if num in lista:
    print(f'O numero {num} está na lista')
else:
    print(f'O numero {num} não está na lista')
    print('--------------------------------')

print(lista)
# Adicionando o numero 22 na lista (valor único) - sempre vai por ultimo na fila
lista.append(22)
# Adicionando uma lista dentro da lista - sempre vai por ultimo na fila
lista.extend([200, 30, 40])
# Adicionando um valor na lista conforme a posição
lista.insert(3, 300)
# Juntando 2 listas
lista3 = lista + lista2

print(lista)
print(lista3)
num = int(input('Digite um numero: '))
if num in lista:
    print(f'O numero {num} está na lista')
else:
    print(f'O numero {num} não está na lista')
    print('--------------------------------')

print('Imprimindo a lista inversa: ')
lista.reverse()
print(lista)
lista3.reverse()
print(lista3)

# copiando uma lista
lista4 = lista3.copy()
print(lista4)

# contando a lista
print(len(lista4))

# Removendo itens da lista
print(lista4)
lista4.pop()
print(lista4)

# zerando a lista
lista4.clear()
print(lista4)

# Repetir elementos em uma lista
print(lista2)
lista2 = lista2 * 4
print(lista2)

