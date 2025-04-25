num = int(input())
num2 = map(int, input().split())

soma = 0
for valor in num2:
    soma += valor

result = soma / num
print(result)
