lista = []
matriz = []
cont = 0
cont2 = 0
op = input()
while cont < 12:
    while cont2 < 12:
        X = float(input())
        lista.append(X)
        cont2 = cont2 + 1
    matriz.append(lista)
    lista = []
    cont = cont + 1
    cont2 = 0
soma = 0
for i in range(12):
    for j in range(12):
        if i != j and i < j:
            soma += matriz[i][j]
if op == "S":
    print("%.1f" % soma)
if op == "M":
    print("%.1f" % (soma/66))
