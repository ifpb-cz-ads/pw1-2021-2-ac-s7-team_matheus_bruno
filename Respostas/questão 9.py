frase = input("Digite uma frase:")
aux = {}
for letra in frase:
    if letra in aux:
        aux[letra] = aux[letra] + 1
    else:
        aux[letra] = 1
print(aux)