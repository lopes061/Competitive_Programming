def tem_numeros_diferentes(ano):
    return(len(set(str(ano)))) == len(str(ano))

y = int(input())
Proximo_ano = y+1
while not tem_numeros_diferentes(Proximo_ano):
    Proximo_ano += 1

print(Proximo_ano)