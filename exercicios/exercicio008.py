 # Escreva um programa que leia um valo em metros e a exiba convertido em centimetros e milimetros

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {} em centimetro é {} e a medida em milimetros é {}'.format(medida, cm, mm))