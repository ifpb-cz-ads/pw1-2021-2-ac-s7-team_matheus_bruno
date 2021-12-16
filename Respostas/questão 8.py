T = [-10, -8, 0, 1, 2, 5, -2, -4]
minima = T[0]
maxima = T[0]
soma = 0
for e in T:
    if e < minima:
        minima = e
    if e > maxima:
        maxima = e
    soma = soma + e
print(f"A temperatura máxima é: {maxima} °C")
print(f"A temperatura mínima é: {minima} °C")
print(f"A temperatura média é: {soma / len(T)} °C")