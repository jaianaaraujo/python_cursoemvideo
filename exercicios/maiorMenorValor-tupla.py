# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
n = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
# Listagem dos números gerados
print('Os valores sorteados foram:')
for numeros in n:
    # O end vai deixá-lo um do lado do outro por conta do espaço que colocamos
    print(f' {numeros}', end=' ')
# Indique o menor e maior valor que estão na túpla
print(f'\n O maior valor sorteado foi {max(n)}')
print(f'\n O menor valor sorteado foi {min(n)}')
