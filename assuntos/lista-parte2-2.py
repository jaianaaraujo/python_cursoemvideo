pessoas1 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas1[0][0]) # eu quero o indice zero da lista pessoas1, e desse indice que peguei, eu quero o indice zero dentro dele
print(pessoas1[1][1]) # aqui será ['Maria', 19] e 19
print(pessoas1[2][0])
totmaiorIdade = 0
for p in pessoas1:
    print(p[0]) # ele vai imprimir o que está no indice zero que são os nomes
for p in pessoas1:
    if p[1] >= 21: # estou validando se o indice 1 de cada lista é maior que 21
        print(f'{p[0]} tem {p[1]} anos de idade')
        totmaiorIdade+=1
print(totmaiorIdade)