# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composto
from random import randint
print('-' * 30)
print('Jogo da mega sena')
print('-' * 30)
lista = list() # crio uma lista
cont = 0 # contador
while True:
    num = randint(1, 60) #randomizar número entre 1 e 60
    if num not in lista: # se esse número selecionado não estiver na lista
        lista.append(num) # Eu vou adicioná-lo na lista que criei
        cont+=1 # se ele for adicionado eu faço um incremento no contador, porque assim me ajudará a dlimitar a quantidade de números selecionados 
    elif cont >= 6: # Se o contador for maior ou igual a 6 ele break, para assim, sortear apenas 6 números 
        break
print(f'Os números sorteados foram: {lista}')

