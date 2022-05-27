salario = float(input('Qual é o salário do funcionário? '))
reajuste = int(input('Qual percentual de reajuste? '))
print(f'O valor atual é: R${(salario * reajuste / 100) + salario}')