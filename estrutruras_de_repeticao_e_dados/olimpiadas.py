def champ(medalhas):
    O = medalhas[min(medalhas)][0]
    P = medalhas[min(medalhas)][1]
    B = medalhas[min(medalhas)][2]
    paises = list(medalhas.keys())
    campeao = paises[0]
    for x in medalhas:
        if medalhas[x][0] > O:
            campeao = x
        elif medalhas[x][0] == O:
            if medalhas[x][1] > P:
                campeao = x
            elif medalhas[x][1] == P:
                if medalhas[x][2] > B:
                    campeao = x
                elif medalhas[x][2] == B:
                    if x < pais:
                        print('ok')
                        campeao = x
    return campeao

n, m = map(int, input().split(' '))
medalhas = {}
pais_medalhas = {}
paises = []
ranking = []

for x in range(m):
    aux = [int(x) for x in input().split(' ')]
    medalhas[x] = aux
    for x in aux:
        if x not in paises:
            paises.append(x)
paises = sorted(paises)
o = p = b = 0

for pais in paises:
    for x in medalhas:
        if medalhas[x][0] == pais:
            o += 1
        if medalhas[x][1] == pais:
            p += 1
        if medalhas[x][2] == pais:
            b += 1
    pais_medalhas[pais] = [o, p, b]
    o = p = b = 0

while len(pais_medalhas) != 0:
    aux = champ(pais_medalhas)
    ranking.append(aux)
    del pais_medalhas[aux]
    if len(pais_medalhas) == 0:
        break

for x in ranking:
    print(x)
