
frase = input().strip()


contador_maiusculas = 0
contador_minusculas = 0

for char in frase:
    if char.isupper():
        contador_maiusculas += 1
    elif char.islower():
        contador_minusculas += 1


if contador_maiusculas > contador_minusculas:
    resultado = frase.upper()  
else:
    resultado = frase.lower()  


print(resultado)

#ou 

frase = input().strip()

contador_maiusculas = len([char for char in frase if char.isupper()])
contador_minusculas = len([char for char in frase if char.islower()])

if contador_maiusculas > contador_minusculas:
    resultado = frase.upper()  
else:
    resultado = frase.lower()  

print(resultado)