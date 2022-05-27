from random import randint
print('''
      Bem-vindos(as) ao jogo Pedra Papel e Tesoura!
            ''')
def menu():
    print(""" OPÇÕES
        [0] Pedra
        [1] Papel
        [3] Tesoura
        """)
menu()
#Escolhas
# Mostrando as opções para o usuário
opcoes = ['Pedra', 'Papel', 'Tesoura']
jogador= int(input('>> Qual dessas opções você escolhe? '))
maquina = randint(0, 2)
print('*=' * 20) 
print(f'Você escolheu a opção {(opcoes[jogador])}')
maquina = randint(0, 2)
print(f'A maquina escolheu {(opcoes[maquina])}')

# pontos
pontosM = 0
pontosJ = 0

# jogo

def jogo():
  while maquina < 3 or jogador < 3:
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

jogo()


