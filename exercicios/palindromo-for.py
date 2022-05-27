# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Qual a frase ou palavra? ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso= ''
for letra in range(len(junto) - 1, -1, -1 ): #Usamos o len para conseguir pegar a última letra, colocamos menos 1, pq o len conta começando com 0
# len(junto) - 1, -1, -1 = Foi da última letra,  até a primeira, voltando uma letra
    inverso += junto[letra]
if junto == inverso:
    print(f'O inverso de {junto} é: {inverso}. É PALÍNDROMO! ')
else:
    print('Não é um palíndromo')


''' 
frase = str(input('Qual a frase ou palavra? ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print(f'O inverso de {junto} é: {inverso}. É PALÍNDROMO! ')
else:
    print('Não é um palíndromo')
'''

   