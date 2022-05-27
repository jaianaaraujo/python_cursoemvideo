n = c = 0
while n == 0:
    num = float(input('Digite um número: '))
    c += num 
    if num == 0:
        break
print(f'O total dos números digitados foi {c}')