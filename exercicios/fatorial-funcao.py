# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False): # O show é para saber se quero mostrar fazendo a conta, ele já começa com false, se colocar verdadeiro então ele mostra
# Por padrão o show é false, ou seja, não mostrará
    f = 1 # que é o último fatorial sempre é 1
    for c in range(n, 0, -1): # O menos 1 para que ele fique de forma decrescente até o número escolhido
        if show:
            print(c, end='')
            if c > 1: # se o contador for maior que 1 então coloca x
                print(' x ', end='')
            else: # mas se o contador for igual a 1 coloca =
                print(' = ', end='')
        f *= c # o f já começa com um, e a cada rodada ele vai multiplicando com o valor daquela nova rodada
    return f

print(fatorial(5, show=True))
