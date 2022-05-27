# -------------- OPERAÇÕES ARITMÉTICAS ---------------------

#          1)     +   = Soma
#          2)     -   = Subtração
#          3)     *   = Multiplicação
#          4)     /   = divisão
#          5)     **  = potência
#          6)     //  = divisão inteira
#          7)     %   = resto


# ---------------- ORDEM DE PRECEDENCIA 

#  1º)   () Parênteses
#  2º)   ** potência
#  3º)  *   /   //    % 
#  4º)  +    -


print(5 + 3 * 2) 
print(5 * 9 / 2 )

# ---------------- CALCULANDO A POTÊNCIA -------------------

pow(2, 3) #dois ao cubo

# --------------- CALCULANDO A RAIZ QUADRADA -----------------

print(8**(1/2))


# ------------- COLOCANDO A QUANTIDADE QUE VOCÊ QUER

print('oi'*5)

# ------------ ALINHANDO -----------

nome = 'Jaiana'
print('O nome dele é {:>20}'.format(nome)) # Alinhamento vai dizer em que opsição você colocará, nesse caso em questão voc~e colocará o nome Jaiana a 20 espaços a direitsa
print('O nome dele é {:=^20}'.format(nome)) # Colocorá Ana em vinte eaços coentralizado exemplo ===========Ana=========



n1 = int(input('Um valor: '))
n2 = int(input('Um valor 2: '))
s = n1 + n2
print('A soma de {} e {} é: {}'.format(n1, n2, s))
print('A soma de {} e {} é: {:.3f}'.format(n1, n2, s))
print('A soma de {} e {} é: {:.3f}'.format(n1, n2, s), end='') #coloco end para que no final ele não quebre linnha, continue norma[

