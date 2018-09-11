def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

n = int(input())
res = fib(n)
if res == 0:
    print("O antidoto nao e necessario")
else:
    print("%d mg/L" %res)
