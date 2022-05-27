num = int(input('Qual o número? '))
operacoes = input("""
                  [+] Adição
                  [-] Subtração
                  [*] Multiplicação
                  [/] Divisão
                  """)
for n in range(1, 11):
    if operacoes == '+':
        print('{} + {} = {}'.format(n, num, num+n))
    elif operacoes == '-':
        print('{} - {} = {}'.format(n, num, num-n))
    elif operacoes == '/':
        print('{} / {} = {}'.format(n, num, num/n) )  # CORRIGIR ESSA PARTE DE DIVISÃO
    elif operacoes == '*':
        print('{} * {} = {}'.format(n, num, num*n))
    else:
        print('Escolha um operador válido: {}'.format(operacoes))
