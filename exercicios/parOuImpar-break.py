# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

v =0
while True:
    jogador = int(input('Diga o valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo= ' '
    while tipo not in 'PpIi': # Se o tipo não tiver PpIi ele ocorrerar o laço
        tipo = str(input('par ou Impar? [P/I]')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você venceu!!')
            v+=1
        else:
            print(f'Você perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Você venceu!!')
            v+=1
        else:
            print(f'Você perdeu!!')
            break
    print('Vamos jogar novamente...')       
print(f'GAME OVER! Você venceu {v} vezes.')