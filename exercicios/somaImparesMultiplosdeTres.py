# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # um acumulador para ir acumulando os valores da rodada do for. Acumula os valores.
contador = 0 # contará quantas vezes encontramos os números multiplos de 3
for n in range(1, 501, 2): # pulará em 2 em 2 
    if n % 3 == 0:
      print(n, end=' ')
      contador += 1
      soma += n 
print('\n Valor total da soma dos números são: {}. E quantas vezes foram encontrados números multiplos três foi: {}'.format(soma, contador))
