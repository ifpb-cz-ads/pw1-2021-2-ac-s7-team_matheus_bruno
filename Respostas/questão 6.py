L = [15, 7, 27, 39]
p = int(input("Digite um valor que vai ser procurado (p): "))
v = int(input("Digite o outro valor que vai ser procurado (v): "))
cont = 0
achouP = False
achouV = False
primeiro = 0
while cont < len(L):
    if L[cont] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[cont] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    cont += 1
if achouP:
    print(f"p: {p} foi encontrado")
else:
    print(f"p: {p} não foi encontrado")
if achouV:
    print(f"v: {v} foi encontrado")
else:
    print(f"v: {v} não foi encontrado")
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")