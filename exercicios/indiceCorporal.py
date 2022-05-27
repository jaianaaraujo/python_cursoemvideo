# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura) # (altura **2)
if imc < 18.5:
    print('IMC abaixo de 18,5: Abaixo do Peso')
elif imc == 18.5 or imc <= 25: # 18.5 <= imc < 25
    print(' Entre 18,5 e 25: Peso Ideal')
elif imc == 30 or imc <= 40: # 30 == imc <= 40
    print('30 até 40: Obesidade')
elif imc >= 40:
    print('Acima de 40: Obesidade Mórbida')

