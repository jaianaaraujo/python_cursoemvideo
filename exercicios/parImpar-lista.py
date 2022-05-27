c = 1
par = []
impar = []
while c <=10:
    num = int(input('Me diga qual é o número?'))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    c+=1
print(f'Lista par: {par}. Lista impar: {impar}')