tab = int(input('Digite um numero para exibir sua tabuada: '))
print("Tabuada do numero ", tab)
for v in range(1, 11, 1):
    print(str(tab) + " x " + str(v) + " = " + str((tab*v)))