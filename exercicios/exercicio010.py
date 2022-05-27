#Conersor de moedas

real = float(input('Quanto dinheiro tem na sua carteira?'))
dolar = real / 3.27

print('Você tem essa valor na carteira R${:.2f} e pode comprar esse valor em dolar {:.2f}'.format(real, dolar))