romano = input()
valores = {"0": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
total = 0
anterior = "0"
aux = 0
for num in romano:
    if num == anterior:
        aux += valores[num]
    else:
        if valores[num] > valores[anterior]:
            total -= aux
        else:
            total += aux
        aux = valores[num]
        anterior = num
total += aux
print(total)
if total % 5 == 0:
    print("O número e múltiplo de 5!")
else:
    print("O resto da divisão por 5 e {}.".format(total % 5))
