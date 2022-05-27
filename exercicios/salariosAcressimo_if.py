# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? '))
if salario <= 2800:
    novo = salario + (salario * 20 / 100)
    print('Quem recebia esse salário R${} terá esse novo salário R${}'.format(salario, novo))
elif salario >= 2800 and salario <= 7000: 
    novo = salario + (salario * 15 / 100)
elif salario >= 15000:
    novo = salario + (salario * 5 / 100)
print('Quem ganhava R$ {} receberá {}'.format(salario, novo))