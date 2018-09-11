def tri(numero):
    tri = 0
    while(numero >= 1):
        tri = tri + numero
        numero = numero - 1
    return tri

numero = int(input())
res = tri(numero)
print(res)
