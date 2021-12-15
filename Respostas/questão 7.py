L = [15, 7, 27, 39]
p = int(input("Digite o valor que vai ser procurado (p):"))
v = int(input("Digite o outro valor que vai ser procurado (v):"))
cont = 0
achouP = -1
achouV = -1
primeiro = 0
while cont < len(L):
    if L[cont] == p:
        achouP = cont
    if L[cont] == v:
        achouV = cont
    cont += 1
if achouP != -1:
    print(f"p: {p} foi encontrado na posição {achouP}")
else:
    print(f"p: {p} não foi encontrado")
if achouV != -1:
    print(f"v: {v} foi encontrado na posição {achouV}")
else:
    print(f"v: {v} não foi encontrado")
if achouP != -1 and achouV != -1:
    if achouP <= achouV:
        print("p foi encontrado antes de v")
    else:
        print("v foi encontrado antes de p")