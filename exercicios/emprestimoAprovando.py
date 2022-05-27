# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prestacao =  casa /(anos * 12) 
porcento = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

if prestacao <= porcento:
    print('Ele não poderá fazer o financiamento.')
else:
    print('Que tal iniciarmos o seu financiamento? :D')
