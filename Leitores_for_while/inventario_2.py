eq = []
vl = []
ns = []
dpt = []

resp = "S"
while resp == "S":
    eq.append(input("Equipamento: "))
    vl.append(float(input("Valor: ")))
    ns.append(int(input("Numero Serial: ")))
    dpt.append(input("Departamento: "))
    resp = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(eq)):
    print("\nEquipamento: ", (indice + 1))
    print("Nome.............: ", eq[indice])
    print('Valor............: ', vl[indice])
    print("Serial...........: ", ns[indice])
    print("Departamento.....: ", dpt[indice])