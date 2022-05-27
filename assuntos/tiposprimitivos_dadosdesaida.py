# ------------ NÚMEROS INTEIROS

n1 = int(input('Digite o número n1:')) #Quando eu dou um input mesmo que seja digitado um numero, ele será considerado como uma string e para resolver isso, por isso utilizamos o tipo primitivo INT para trasnformar essa string em inteiro 
n2 = int(input('Digite o número n2'))
s = n1 + n2 #aqui ele não está somando está concatenando, resolveremos isso abaixo
print('A soma é: {}'.format(s))
#print('A soma é:', s) = Outra forma de fazer
print('A soma entre {} e {}, vale {}'.format(n1, n2, s))

# -------------OS 4 TIPOS PRIMITIVOS

#            1) int = Números inteiros
#            2) float = Números décimais
#            3) bool = Booleano (True ou false) o verdadiro ou falso, a letra inicial sempre tem ser maiusculo
#            4) str = String 

numero = float(input('Qual o número para ser convertido?'))
print(numero)
print(type(numero)) #Para saber o tipo


#-------------  PARA SABER SE É NUMERICO ------------

numero1 = input('Qual o numero?')
print(numero1.isnumeric()) # Ele responderá com um boleano informando se é verdadeiro ou falso


# -------------- PARA SABER SE ELE É LETRA -------------

numero2 = input('Qual o numero')
print(numero2.isalpha())

# ------------ PARA SABER SE É ALPHANUMERICO

numero3 = input('Qual o número?')
print(numero3.isalnum())