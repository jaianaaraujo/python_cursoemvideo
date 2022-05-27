# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = total = quant = 0 # porque todas iniciam com o mesmo valor atribuido

while True: # Se for diferente de 999
    n = int(input('Digite o número que você deseja calcular:  '))
    if n == 999: # uma condicional para quando chegar em 999 ele parar
        break
    total+=n # coloquei embaixo da condição if para não calcular o 999
    quant+=1 # para calcular as vezes de inserção de números
print(f'O total de números inseridos foi {quant} e o total calculado foi {total}')