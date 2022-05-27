#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Já deixo a matriz pré estabelecida
for linha in range(0, 3): # crio um for de linhas 
    for coluna in range(0, 3): # dentro do for de linhas eu crio um for de colunas
        matriz[linha][coluna] = int(input(f'Digite um valor: para [{linha}, {coluna}] ')) # e dentro desse for de colunas a cada uma das 3 rodadas aqui pego um numero e coloca na linha
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
