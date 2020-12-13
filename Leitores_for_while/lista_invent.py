inv = []
resp = "S"
while resp == "S":
    inv.append(input("Equipamento: "))
    inv.append(float(input("Valor: ")))
    inv.append(int(input("Numero Serial: ")))
    inv.append(input("Departamento: "))
    resp = input("Digite \"S\" para continuar: ").upper()

for elem in inv:
    print(elem)