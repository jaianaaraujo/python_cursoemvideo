# JOGO DE PEDRA PAPEL E TESOURA
""" 1) O usuário vai informar por meio de um input (esse input precisa escolher entre as opções que eu der / validação)
2) O computador sorteará

 """
import random
# ESCOLHA DO USUÁRIO


def input_valido(opcoes):
    # o join vai separar as opções que darei
    escolha_usuario = input(f'Escolha a sua opção: {"/".join(opcoes) }')
    while escolha_usuario not in opcoes:
            # ela terá que escolher ima opção que esteja dentro das opções
            escolha_usuario = input(
                f'Opção inválida. Escolha uma opção válida: {"/".join(opcoes) }')
    else:
        return escolha_usuario


# CONFERIR A JOGADA

def conferir_jogada(escolha_usuario, escolha_computador):
   if escolha_usuario == escolha_computador:
       return 'Deu Empate!!'
   elif escolha_usuario == 'pedra':
        if escolha_computador == 'papel':
            return 'Você perdeu!'
        if escolha_computador == 'tesoura':
            return 'Você ganhou!'
   elif escolha_usuario == 'papel':
        if escolha_computador == 'pedra':
            return 'Você ganhou!'
        if escolha_computador == 'tesoura':
            return 'Você perdeu!'
   elif escolha_usuario == 'tesoura':
        if escolha_computador == 'pedra':
            return "Você perdeu!"
        else:
            return "Você ganhou!"


# PROGRAMA PRINCIPAL
# dentro do programa eu posso criar  a escolha computador 
# e perguntar se o usuário quer continuar ou não o jogo

def jokepon():
    # saber se o usuário quer continuar jogando
    quer_jogar= 's' # o quer jogar já começa com sim, para ter a primeira jogada
    while quer_jogar == 's': # enquando for sim
        opcoes = ['pedra', 'papel', 'tesoura']
        escolha_usuario = input_valido(opcoes)
        escolha_computador= opcoes[random.randint(0, len(opcoes)-1)] # opcoes é uma lista, e por ser uma lista na hora de rondomizar irei rondomizar o indice dela e por isso logo após o nome da lista coloco os comandos entre []
        print('*+' * 20)
        print(f'O computador jogou: {escolha_computador}')
        print('*+' * 20)
        print(conferir_jogada(escolha_usuario, escolha_computador))
        quer_jogar = input('Deseja jogar novamente?  [s/n] ')

    while quer_jogar != 's' and quer_jogar != 'n':
        quer_jogar = input('Deseja jogar novamente?  [s/n] ')
    else: 
        print('Obrigado por jogar!!!')

jokepon()