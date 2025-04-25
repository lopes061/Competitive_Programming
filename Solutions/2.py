matriz = [list(map(int,input().split())) for next in range (5)]

for i in range(5):
    for j in range(5):
        if matriz[i][j] == 1:
            linha_um, coluna_um = i, j
            break
movimentos = abs(linha_um - 2)+ abs(coluna_um - 2)


print(movimentos)