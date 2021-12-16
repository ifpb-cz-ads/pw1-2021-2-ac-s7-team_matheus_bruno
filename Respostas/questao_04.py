"""  
4) Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses 
foram abertos e fechados na ordem correta. Exemplo:

(()) OK
()()(()()) OK
()) Erro

"""

expres = str(input('Digite a expressão: '))
pilha = []
for simb in expres:
    abertos = 0
for parentese in expres:
    if parentese == '(':
        abertos += 1
    elif parentese == ')':
        abertos -= 1
        if abertos < 0:
            break

print('balanceado' if abertos == 0 else 'desbalanceado')
