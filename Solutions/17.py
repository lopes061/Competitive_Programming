n = int(input())

somae = 0
somad = 0
count = 0

for i in range(n):
    inp = input().split()
    e = int(inp[0])
    d = int(inp[1])
    somae += e
    somad += d

if somae <= n / 2:
    count += somae
else:
    count += n - somae

if somad <= n / 2:
    count += somad
else:
    count += n - somad


print(count)
