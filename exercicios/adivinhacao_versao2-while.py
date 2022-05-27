# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print(""" Sou seu computador...
      Acabei de pensar em um número entre 0 e 10.
      Será que você consegue advinhar?
            """)
computador = randint(1, 10)
palpites = 0
acertou = False # não acertou ainda
while not acertou:
    jogador = int(input(f'Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} palpites. Parabéns!!')
