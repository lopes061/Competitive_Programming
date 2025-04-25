n = int(input())
count = 0
lista = []

inp = input().split()
lista = [int(x) for x in inp]

if n > 1:
    current_max = lista[0]
    current_min = lista[0]

    for i in range(1, n):
        if lista[i] > current_max:
            count += 1
            current_max = lista[i]
        elif lista[i] < current_min:
            count += 1
            current_min = lista[i]

print(count)
