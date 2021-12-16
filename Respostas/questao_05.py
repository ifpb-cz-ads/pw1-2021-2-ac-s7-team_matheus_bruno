"""  
5) Modifique o programa abaixo de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. 
Dica: observe a condição de saída do while.

L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
achou=False
x=0
while x<len(L):
	if L[x]==p:
    		achou=True
    		break
    	x+=1
if achou:
	print("%d achado na posição %d" % (p,x))
else:
	print("%d não encontrado" % p)

"""

L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
achado = 0

x=0
while x<len(L):
    if L[x]==p:
        achado = 1
        break
    x+=1

if achado == 1:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)