

num1 = input()  
num2 = input()  

result = ''
for c1, c2 in zip(num1, num2):
    if c1 == c2:
        result += '0'
    else:
        result += '1'

print(result)

#Ou 

def function(input1,input2):
    resposta = []
    for c1,c2 in range(len(input1)):
        if c2 == input2[c1]:
            resposta.append("0")
        else:
            resposta.append("1")
    return "".join(resposta)

