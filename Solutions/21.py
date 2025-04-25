s1,s2,s3,s4 = map(int,(input().split()))
count = 0
if s1 == s2 or s1==s3 or s1==s4:
    count+=1
if s2==s3 or s2 == s4:
    count+=1
if s3 == s4:
    count+=1

print(count)