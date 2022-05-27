#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random 
from time import sleep #faz o computador esperar por alguns segundos para executar tal coisa

mensagem = print('Maquina: - Vou pensar em um número entre 0 e 3. Escolha!')
nome = str(input('Qual o seu nome?'))
usuario = int(input('Qual número você acha que a máquina escolheu?'))
sleep(1)
processando = print('PROCESSANDO...')
sleep(3) # Ele vai dar 3 segundos para poder executar o código abaixo
maquina = random.randint(0, 3)
if usuario == maquina:
    print("{} ganhoooou!!!!!!!!!".format(nome))
else:
    print('Maquina ganhoooooooou! EITAAAAAAAAAAAA!')

