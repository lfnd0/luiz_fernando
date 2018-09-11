def quant(idade):
    if idade <= 2:
        return 9
    else:
        return 6

idade = 0
fraldas_dia = []

while True:
    idade = int(input())
    continua = input().lower()
    fraldas_dia.append(quant(idade))
    if continua == 'não':
        break

total = (sum(fraldas_dia)) * 30
n = 0

while n * 100 < total:
    if n * 100 < total:
        n += 1
    if n * 100 >= total:
        break

print(n)
print(n * 100 - total)
