type([])
lista1 = [1, 10, 30, 3, 20, 3]
lista2 = ['D', 'a', 'n', 'i', 'l', 'o']
lista3 = []
lista4 = list(range(12))
lista5 = list('Danilo Silva')

#Encontrando ocorrencias na lista
num = 20
if num in lista4:
    print(f'O numero {num} está na lista')
else:
    print(f'O numero {num} não está na lista')

#Ordenando listas
lista1.sort()
print(lista1)

# contar ocorrencias na lista
print(lista1.count(3))
print(lista5.count('i'))

#Adicionar elementos na lista

print(lista1)
lista1.append(100)
print(lista1)

