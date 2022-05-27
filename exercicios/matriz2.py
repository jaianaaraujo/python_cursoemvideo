""" Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maiorValor = somaColuna = 0
# LENDO A MATRIZ E PREENCHENDO
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira o número: [{linha}, {coluna}] '))
print('-=' * 30)
#Eu crio um novo for para imprimir 
# Para imprimir a matriz completa e não somente a rodada final

#ESCREVENDO ACADA LINHA E COLUNA COM OS NÚMEROS
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()

#A SOMA DOS PARES
print(f'A sma dos números pares são: {somaPar}')
#  A SOMA DOS VALORES DA TERCEIRA COLUNA
for linha in range(0, 3): #Vou passando para cada linha
    somaColuna += matriz[linha][2] # em em cada linha vou somando os valores que estarão na coluna 2
print(f'A soma doas valores da terceira coluna são: {somaColuna}')
# O MAIOR VALOR DA SEGUNDA LINHA 
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor dessa linha é o {maior}.')