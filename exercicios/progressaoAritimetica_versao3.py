# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('*' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1 # a cada volta ele vai incrementando no computador
total = 0
mais = 10
while mais != 0: # enquanto mais for diferente que 0
    total = total + mais # o total será ele somado com o novo valor que o usuário colocar
    while cont <= total: # inicialmente ele limita-se com o número 10
        print(f'{termo} ->', end='') # vai imprimir o termo
        termo += razao # somando o termo com a razão
        cont+=1 # O contador
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

