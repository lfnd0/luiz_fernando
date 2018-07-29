peso = int(input())
capacidade = 560
soma = 0
cont = 0

while (peso != 0 and cont<7) and soma<capacidade:
    soma = soma + peso
    cont = cont + 1
    peso = int(input())
print(cont)
print("%.1f" %soma)
