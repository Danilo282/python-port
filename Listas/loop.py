cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


print('----------------Gerando Indices em um loop For------------------------------------------------')
for indice, cor in enumerate(cores):
    print(indice, cor)

print('----------------------------listas aceitam repetições------------------------------------------')
"""" ('----------------------------se o indice nao estiver na lista, gera valueError-------------------------')"""

""" num = [1, 2, 0, 3, 3, 5, 7]
print(num.index(10)
    Traceback (most recent call last):
    print(num.index(10))
ValueError: 10 is not in list
"""



