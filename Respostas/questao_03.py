"""  
3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = list(range(0,5))
for i in range(5):
    lista3[i] = (lista1[i]**2) + (lista2[i]**2)
    i+=1
print(lista3)