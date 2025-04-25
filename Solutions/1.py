testes  = int (input())
a_total = 0
b_total = 0
c_total = 0

for i in range(testes):
    a,b,c = map(int,input().split())
    
    a_total += a
    b_total += b
    c_total += c

if a_total == 0 and b_total == 0 and c_total == 0:
    print("YES")
else:
    print("NO")