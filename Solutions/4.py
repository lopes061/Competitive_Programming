codigo =input()
resultado = ''
i = 0
while i <len(codigo):
        if codigo[i] == '.':
            resultado += '0'
            i+=1
        
        elif codigo[i] == '-':
            if i+1 < len(codigo) and codigo[i+1] == '.':
                resultado += '1'
                i+=2
            elif i+1 < len(codigo) and codigo[i+1] == '-':
                resultado += '2'
                i+=2
                
print(resultado)