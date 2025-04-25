inp = input()  
saida = inp.replace("+", "")  
saidanum = [int(digito) for digito in saida]  


n = len(saidanum)
for i in range(n):
    for j in range(0, n - i - 1):
        if saidanum[j] > saidanum[j + 1]:
            saidanum[j], saidanum[j + 1] = saidanum[j + 1], saidanum[j]


resultado = ""
for i in range(len(saidanum)):
    resultado += str(saidanum[i])
    if i < len(saidanum) - 1:
        resultado += "+"

print(resultado)
