# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(':=^40'.format('Lojas dos Araújo'))
preco = float(input('Preço das compras: R$ '))
print("""
      [1] à vista dinheiro/cheque: 10% de desconto
      [2] à vista no cartão: 5% de desconto
      [3] em até 2x no cartão: preço formal
      [4] 3x ou mais no cartão: 20% de juros
            """)
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 /100)
elif opcao == 2:
    total = preco - (preco - 5 /100)
elif opcao == 3:
    total = preco / 2
elif opcao ==4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input( 'Quantas parcelas? '))
    parcela = total / totalParcelas
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
