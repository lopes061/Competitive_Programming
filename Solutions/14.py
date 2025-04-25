
n = int(input().strip())
lista = list(map(int, input().split()))
altura_max = max(lista)
altura_min = min(lista)

posicao_altura_max = lista.index(altura_max)
posicao_altura_min = -1
for i in range(len(lista)-1,-1,-1):
    if lista[i] == altura_min:
        posicao_altura_min = i
        break

if posicao_altura_max > posicao_altura_min:
   
    swaps = posicao_altura_max + (n - 1 - posicao_altura_min)-1
else:
    
    swaps = posicao_altura_max + (n - 1 - posicao_altura_min)
    
print(swaps)


