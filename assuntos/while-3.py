# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

cont = 1 # contador
while cont <= 10: # enquanto o contador for menor ou igual a 10
    print(cont, '-> ', end=' ')# ele imprimirá o valor atual do cont, com uma seta e depois seguido de um espaço
    cont +=1 # E a cada rodade ele vai incrementando
print('Acabooou!!') # quando o while atingir o limite estipulado, o programa sairá e ativará o print 

