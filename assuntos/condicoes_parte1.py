# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

tempo = int(input('Quantos anos de uso tem o meu carro?'))
if tempo <= 3:
    print('Ele é novo, tem apenas {} anos de uso'.format(tempo))
else:
    # Na condicional o comando que está mais para dentro, ele pode ser executado ou não.
    print('O carro é velho, ele tem {} anos de uso'.format(tempo))
# Na condicional o comando que está a esquerda sempre será executado
print('----FIIIIM----')


# ----------------- CONDIÇÃO SIMPLIFICADA

print('Carro Novo' if tempo <= 3 else 'Carro usado')
print('--- FIM ---')

print('Não compre outro' if tempo <= 5 else 'Compre um novo')


# ================== EXERCICIO ==============

nome = str(input('Qual é seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem.')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))


# ========== EXERCICIO 2 ==============
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('{} a sua média foi {:.1f}'.format(nome, m))
if m>=6.0:
    print('Aprovadooooo!!! Sua média é: {}'.format(m))
else:
    print('Estude mais e mais!!!! Se esforce!')

# === USANDO IF SIMPLIFICADO

print('Parabéns' if m>=6.0 else 'Estude mais!!')