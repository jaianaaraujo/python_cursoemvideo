#porcentagem / desconto

produto = float(input('Qual valor do produto?'))
desconto = int(input('Valor do desconto?'))
calculo = produto - ((produto * desconto) / 100)

print('O produto tem esse valor: R$ {:.2f} e com o desconto de {} fica no valor de R$ {:.2f}'.format(produto, desconto, calculo ))

