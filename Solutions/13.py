n = int(input())
if n%2:
    print("-1")
    
lista = list(range(1,n+1))
    
for i in range (0,n,2):
    lista[i+1], lista[i] = lista[i], lista[i+1] 

print(lista)
