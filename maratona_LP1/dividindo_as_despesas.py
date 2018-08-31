c = 0
d = 0
i = 0
total = 0
while i <= 5:
    valor = float(input())
    nome = input()
    if (nome == "Clara"):
        c += valor
    else:
        d += valor
    total += valor
    i += 1

if c == d:
    print("MORADORAS QUITES")
elif c < d:
    print("CLARA\n%.2f" % ((total / 2) - c))
else:
    print("DIANA\n%.2f" % ((total / 2) - d))
