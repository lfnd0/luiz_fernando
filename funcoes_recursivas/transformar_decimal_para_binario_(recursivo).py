def binario(n):
    n = bin(n)
    n = str(n[2:])
    for i in range(len(n)):
        print(n[i])

n = int(input())
binario(n)
