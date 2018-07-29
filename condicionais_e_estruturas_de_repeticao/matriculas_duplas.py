p2 = input()
p2 = p2.split(' ')
p2 = list(map(int, p2))

p3 = input()
p3 = p3.split(' ')
p3 = list(map(int, p3))

duplicado = []

for aluno_p2 in p2:
    for aluno_p3 in p3:
        if aluno_p2==aluno_p3 and aluno_p2 not in duplicado:
            duplicado.append(aluno_p2)
            break
duplicado = str(duplicado).strip('[]').replace(',', '')
print(duplicado)
