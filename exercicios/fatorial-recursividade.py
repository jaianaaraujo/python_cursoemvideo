# RECURSIVIDADE

""" 
1) Recursão é um método de simplificação que consiste em dividir um problema em subproblemas do mesmo tipo
2) Os subproblemas são resolvidos, e seus resultados combinados
3) Uma função recursiva é uma função que chama a si própria quando invocada
4) Uma definição de função recursiva possui um ou mais casos-bases, para os quais a função produz um resultado diretamente (sem recursão), em um ou mais casos recursivos.
 """


    
def fatorial(n):
    #caso base
    # O fatorial de um número é calculado pela multiplicação desse número por todos os seus antecessores até chegar ao número 1. Note que nesses produtos, o zero (0) é excluído.
    if n == 0 or n == 1: # esses números não tem antecessores para serem calculados, por lógica se o usuário escolhê-los o resultado será 1
        return 1
    else: # caso recursivo / se o usuário escolher número diferente de 1 ou 0, então existem números antecessores para serem multiplicados, e aí chamamos a recursão, que é a mesma função dentro dela mesma
        return n * fatorial(n - 1)

n = int(input('Número para cacular fatorial? ')) # O usuário vai escrever o número que ele quer para fazer o fatorial
resposta = fatorial(n) # coloco como parâmetro do fatorial o número que o usuário inserir
print(f'O fatorial de {n} é {resposta}')