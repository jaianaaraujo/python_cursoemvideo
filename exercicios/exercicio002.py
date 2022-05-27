nome = input('Qual o seu nome')
saudacao = 'Seja bem-vinda(o),'
print(saudacao, nome)

#No Python tem como fazer utilizando a formatação 

nomeusuario = input('Qual o seu nome?')
idade  = input('Qual sua idade')
saudacaousuario = input('Seja bem-vinda(o), {} {}!'.format(nome, idade)) #o format irá colocar o valor da variável nome dentro das chaves
#O format vai inserir o valor dentro do espaço resevado