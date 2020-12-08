id = int(input('Digite a sua idade: '))
ts = int(input('Digite o tempo de serviço: '))
idts = id + ts

if idts >= 85 or id >= 65 or ts >= 30:
    print('Pode se aposentar.')
else:
    print('Não pode se aposentar.')