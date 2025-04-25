matriz = [list(map(int, input().split())) for _ in range(3)]

luzes = [[1 for _ in range(3)] for _ in range(3)]

def alternar_luz(i, j):
    luzes[i][j] = 1 - luzes[i][j]
    
    if i > 0:
        luzes[i - 1][j] = 1 - luzes[i - 1][j]
    if i < 2:
        luzes[i + 1][j] = 1 - luzes[i + 1][j]
    if j > 0:
        luzes[i][j - 1] = 1 - luzes[i][j - 1]
    if j < 2:
        luzes[i][j + 1] = 1 - luzes[i][j + 1]

for i in range(3):
    for j in range(3):
        for _ in range(matriz[i][j]):
            alternar_luz(i, j)

for linha in luzes:
    print(''.join(map(str, linha)))

