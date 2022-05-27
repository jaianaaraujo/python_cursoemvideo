""" Desenha uma matriz """

linhas = int(input("Quantidade de linhas : "))
colunas = int(input("Quantidade de colunas : "))

for i in range(((colunas)  * 2) + 1 ):
    print("-", end = "")
print()
for i in range(linhas):
    for j in range(colunas + 1 ):
        print("|", end = "")
        print(" ", end = "")
    print()
    print("|", end = "")
    for k in range(((colunas)  * 2) - 1 ):
        print("-", end = "")
    print("|", end = "")
    print()
