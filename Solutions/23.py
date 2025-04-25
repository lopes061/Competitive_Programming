nome_usuario = input().strip()

caracteres_distintos = len(set(nome_usuario))

if caracteres_distintos % 2 == 0:
    print("BATE-PAPO COM ELA!")
else:
    print("IGNORE-O!")


#ou 


nome_usuario = input().strip()


caracteres_vistos = []


for caractere in nome_usuario:
    if caractere not in caracteres_vistos:
        caracteres_vistos.append(caractere)


caracteres_distintos = len(caracteres_vistos)


if caracteres_distintos % 2 == 0:
    print("BATE-PAPO COM ELA!")
else:
    print("IGNORE-O!")
