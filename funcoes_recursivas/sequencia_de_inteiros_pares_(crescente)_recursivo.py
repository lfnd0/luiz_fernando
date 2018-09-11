def sequencia(n):
    i = 0
    for i in range(0, n+1):
        if i%2==0:
            print(i)
        i += 1

n = int(input())
sequencia(n)
