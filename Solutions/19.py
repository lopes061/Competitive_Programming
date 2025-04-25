n = int(input())
result = 0 
result_max = 0

for i in range(n):
    inp = input().split()
    saiu = int(inp[0])
    entrou = int(inp[1])
    
    result = result + entrou - saiu
    if result >= result_max:
        result_max = result    
        
print(result_max)