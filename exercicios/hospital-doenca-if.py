''' Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:

a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças
 '''

dor = input('Sente dor no corpo? [S/N] ').upper().strip()
febre = input('Sente febre? [S/N] ').upper().strip()
tosse = input('Sente tosse? [S/N]  ').upper().strip()
cNasal = input('Está comcongestão nasal? [S/N] ').upper().strip()
manchas = input('Está com manchas no corpo? [S/N]  ').upper().strip()


if  dor == 'S' and febre == 'S' and tosse == 'N' and cNasal == 'N' and manchas == 'S':
   print('Dengue ')
elif dor == 'S' and febre == 'S' and tosse == 'S' and cNasal == 'S' and manchas == 'N':
    print('Gripe')
elif dor == 'N' and febre == 'S' and tosse == 'S' and cNasal == 'S' and manchas == 'N':
    print('Gripe')
elif dor == 'S' and febre == 'N' and tosse == 'N' and cNasal == 'N' and manchas == 'N':
    print('Sem doenças')
elif dor == 'N' and febre == 'N' and tosse == 'N' and cNasal == 'N' and manchas == 'N':
    print('Sem doenças')