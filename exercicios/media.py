# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

pnota = float(input('Primeira nota: '))
snota = float(input('Segunda nota: '))
snota3 = float(input('Terceira nota: '))
media = (pnota + snota + snota3) / 3
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(pnota, snota, media))
if media < 5:
    print('Reprovado!!')
elif media >= 6:
    print('Aprovado!!')