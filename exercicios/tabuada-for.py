# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Qual o número? '))
for n in range(1, 11):
    print('{} * {} = {}'.format(num, n, n*num))