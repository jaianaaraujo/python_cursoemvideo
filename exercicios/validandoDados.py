# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

""" 

def leiaInt():
    n = input('Digite um número: ').strip()[0]
    n = int(n)
    if n == '':
          n = input('Digite um número: ').strip()[0]
    print(n)
leiaInt() """



def leiaInt(msg): # criando uma função que receberá uma mensagem
    ok = False # o ok ele é falso
    valor = 0 # valor é zero
    while True: 
        n = str(input(msg)) # ele pegará um número do usuário
        if n.isnumeric(): # se essa mensagem for um número
            valor = int(n) # passa esse número para o valor como inteiro
            ok = True # e ok se transforma em verdadeiro
        else:
            print('Digite um número inteiro Várido.')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')#uma forma de transformar a função como input
print(f'Você acabou de digitar o número: {n}')