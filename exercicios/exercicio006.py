#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Qual seu número'))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero ** (1/2)

print('O número digitado foi {}, o seu dobro é: {}, o seu triplo é: {} e a raiz quadrada é: {}'.format(numero, dobro, triplo, raizquadrada))