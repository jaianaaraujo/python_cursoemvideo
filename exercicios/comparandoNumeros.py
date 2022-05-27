# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais


primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
if primeiro > segundo:
    print('O primeiro numero {} é maio que o segundo numero {}'.format(primeiro, segundo))
elif segundo > primeiro:
    print('O segundo {} é maor que o primeiro {}'.format(segundo, primeiro))
else:
    print('Eles são iguais! Tente novamente!')

