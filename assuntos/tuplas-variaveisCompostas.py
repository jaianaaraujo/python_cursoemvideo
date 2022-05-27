''' Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais. '''

''' 
1) Existe em Python 3 tipos de variáveis compostas, que são:
                a) Tuplas
                b) Listas
                c) Dicionários
                

A) TUPLA:
    São enumerados através de indices, e os indices começam a contar do zero. 
    * Túplas são imutáveis 
    * Toda tupla é entre parentese e depois do Python 3.5 não precisa mais colocar parentese.
    * No Python, posso começar uma variável composta de 3 formas: [lista], (tupla) ou {dicicionario}
'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# MANIPULAÇÃO DE TUPLAS
print('+=' * 20)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3]) # vai mostrar o suco e a pizza, ele desconsidera o 3
print(lanche[:2]) # vai mostrar do hambúrguer e suco

# TUPLAS SÃO IMUTÁVEIS

## lanche[1] = 'Refrigerante' # dará um erro, pq tuplas são imutáveis

# FOR
print('+=' * 20)
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi para carammba!')

print('+=' * 20)

for com in range(0, len(lanche)):
    print('-'.join(lanche))

print('+=' * 20)

for comidaa in lanche:
    print(f' Comer: {comidaa}')

print('+=' * 20)
print('>>>>>>>> PRIMEIRA FORMA DE MOSTRAR O VALOR E A SUA POSIÇÃO')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
print('+=' * 20)
print('>>>>>>> SEGUNDA FORMA DE MOSTRAR O VALOR E A SUA POSIÇÃO')
for pos, comida in enumerate(lanche): # Nesse caso aqui, utilizo o enumerate para enumerar, e no for tenho que colocar duas variáveis sepradas por virgula
    print(f'Eu vou comer {comida} na posição {pos}')
    
print('+=' * 20)
print('>>>>>>>> CONCATENANDO COM TUPLAS')
a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 90)
c = a + b
print(c)
print(len(c))
print(c.count(5)) #quantas vezes aparece o numero 5
print(c.index(8)) # Em que posição está o número 8 - ele mostrará o indice
print(c.index(2, 4)) # quando localização do indice do numero depois a partir da posição 4