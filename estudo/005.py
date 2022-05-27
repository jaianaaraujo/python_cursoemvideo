
def calc_fatorial(num:int) -> int:
    if num == 0:
        return 1
    else:
        return num * calc_fatorial(num-1)

print(calc_fatorial(15))