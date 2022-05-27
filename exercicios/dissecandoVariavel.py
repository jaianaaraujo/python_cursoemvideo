# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

digite = input('Digite algo, por favor:')
print('Só tem espaços? {}'.format(digite.isspace()))
print('É um número? {}'.format(digite.isnumeric()))
print('É um alfabeto? {}'.format(digite.isalpha()))
print('É um alphanumerico? {}'.format(digite.isalnum()))
print('Está em maiúsculo? {} '.format(digite.isupper()))
print('Está em minúsculo? {}'.format(digite.islower()))
print('está capitalizado'.format(digite.istitle())) #Se a primeira letra é maiuscula

