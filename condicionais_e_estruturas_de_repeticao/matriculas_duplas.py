p2 = input()
p2 = p2.split(' ')
p2 = list(map(str, p2))

p3 = input()
p3 = p3.split(' ')
p3 = list(map(str, p3))

duplicado = []
n = ''

for aluno_p2 in p2:
    for aluno_p3 in p3:
        if aluno_p2 == aluno_p3:
            n = n + str(aluno_p2) + ' '
print(n)
