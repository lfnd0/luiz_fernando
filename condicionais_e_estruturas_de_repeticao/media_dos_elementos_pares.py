lista = input()
lista = lista.split(' ')
lista = list(map(int, lista))

i = 0
cont = 0
soma = 0
media = 0

for i in range(len(lista)):
    if lista[i]>0 and lista[i]%2==0:
        soma = soma+lista[i]
        cont = cont+1
        i = i+1
try:
    media = soma/cont
    print("%.2f" %media)
except ZeroDivisionError:
    print("-1")
