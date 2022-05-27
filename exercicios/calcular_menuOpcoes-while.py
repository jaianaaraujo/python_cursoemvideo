''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(""" 
        [1] Somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa      
        """)
    opcao = int(input('>>>>>>>> Qual é a sua opções? '))
    if opcao ==1:
        soma = n1 + n2
        print(f'A soma é {soma}')
        print('=-=' * 10)
    elif opcao ==2:
        print('A multiplicaçãoé: ', n1 * n2)
        print('=-=' * 10)
    elif opcao ==3:
        if n1 > n2:
            print(f'O  {n1} é maior que {n2}')
            print('=-=' * 10)
        elif n1 < n2:
            print(f'O  {n2} é maior que {n1}')
            print('=-=' * 10)
        else:
            print('Não existe maior enre eles, pois são identicos!')
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    else:
        print('Opção inválida!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
