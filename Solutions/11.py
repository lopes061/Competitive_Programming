inp = input().split()
n = int(inp[0])
m = int(inp[1])

def is_prime(num):

    for i in range(2, num):
        if(num%i==0):
           return False

    return True

next_prime = None

for i in range(n + 1, m + 1):
    if is_prime(i):
        next_prime = i
        break

if next_prime == m:
    print("YES")
else:
    print("NO")