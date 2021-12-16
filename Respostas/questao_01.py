"""  
1) Modifique o programa abaixo para ler 7 notas em vez de 5.

notas=[0,0,0,0,0]
soma=0
x=0
while x<5:
	notas[x]=float(input("Nota %d:" % x))
	soma += notas[x]
	x+=1
x=0
while x<5:
	print("Nota %d: %6.2f" % (x, notas[x]))
	x+=1
print("Média: %5.2f" % (soma/x))

"""
notas = list(range(0,7));
soma = 0;
for x in range(0,7):
    notas[x] = float(input("Nota %d: " % x));
    soma += notas[x]
    x+=1;

for x in range(0,7):
    print("Nota %d: %0.2f" % (x, notas[x]));
    x+=1;
print("Média: %0.2f"%(soma/x));

