# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('a')))

print('A primeira letra [a] apareceu na posição {}'.format(frase.find('a')))
print('A primeira letra [a] apareceu na posição {}'.format(frase.rfind('a')))
