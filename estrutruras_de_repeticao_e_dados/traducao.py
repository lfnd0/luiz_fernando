n, m = 0, 1

while n != m and m != 0:
    n, m = map(int, input().split(' '))

    if n == m and m == 0:
        break

    regras = []
    texto = []

    for x in range(n):
        aux = input()
        regras.append(aux.split(' -> '))

    for x in range(m):
        aux = input()
        texto.append(aux)
    verificar = []
    for x in range(len(texto)):
        for i in range(len(regras)):
            aux = texto[x].replace(regras[i][0], regras[i][1])
            texto[x] = aux
    for x in texto:
        print(x)
