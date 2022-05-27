# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
# O while pode ser usando quando eu sei o limite e também quando eu não sei o limite


c=1 # precisa de um contador 
while c !=10: # enquanto o contador for diferente de 10 / é conhecido como condição de parada
     print(c)  
     c+=1
print('Acabou')

# ========== SEGUNDA FORMA DE FAZER ===========

r = 'S'

while r == 'S': # enquanto r for igual a S 
    n = int(input('Digite um valor')) # pergunta o valor
    r = str(input('Quer continuar? [S/N] ')).upper() # mas se ele escrever N, não perguntará mais o valor e finaliza
print('Fiiim!!')

''' 
c = 1
while c < 10:
    print(c)
    c= c +1
print('Fim!!')


'''