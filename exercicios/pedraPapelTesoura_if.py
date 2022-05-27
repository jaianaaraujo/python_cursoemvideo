# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você

# Importando bibiotecas
from random import randint

# Mostrando as opções para o usuário
print("""
      [0] Pedra
      [1] Papel
      [3] Tesoura
      """)
opcoes = ['Pedra', 'Papel', 'Tesoura']  # lista de opções
# Jogador escolhendo
jogador = int(input('Qual a sua jogada? '))
print('*=' * 20)  # Criando divisão no terminal
print('Você escolheu a opção {}'.format(opcoes[jogador]))
maquina = randint(0, 2)
# Máquina esclhendo
print('A maquina escolheu {}'.format(opcoes[maquina]))
print('*=' * 20)
# Resultado da jogada
print('========> RESULTADO: ')
# Condições
if maquina == 0: # PEDRA
    if jogador == 0:
        print('Empate!!!!')
    elif jogador == 1:
        print('Jogador venceeeeu! Uhuuuuu!!!')
    elif jogador == 2:
        print('Máquina venceeeeu! Vamos que vamos!!')
    else:
        print('Xiiiii, jogada inválida!!!!')
elif maquina == 1: # PAPEL
    if jogador == 0:
        print('Máquina venceeeeu! Uhuuuuu!!!')
    elif jogador == 1:
        print('Empate!!!!')
    elif jogador == 2:
        print('Jogador venceeeeu! Vamos que vamos!!')
    else:
        print('Xiiiii, jogada inválida!!!!')
elif maquina == 2: # TESOURA
    if jogador == 0:
        print('Jogador venceeeeu! Uhuuuuu!!!')
    elif jogador == 1:
        print('Máquina venceeeeu! Vamos que vamos!!')
    elif jogador == 2:
        print('Empate!!!!')
    else:
        print('Xiiiii, jogada inválida!!!!')
