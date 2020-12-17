import datetime
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
id = atual - nasc

print('O atleta tem {} anos. '.format(id))
if id <= 4:
    print('Não apto a nadar.')
elif id <= 5:
    print('Infantil A')
elif id <= 8:
    print('Infantil B')
elif id <= 11:
    print('Juvenil A')
elif id <= 14:
    print('Juvenil B')
elif id <= 17:
    print('Senior')
