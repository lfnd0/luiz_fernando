n = int(input())
valor = input()
valores = list(map(int,valor.split(' ')))
tamanho = len(valores)
pAtual = 0
pMaior = 0
for i in range(0,tamanho-1,1):
    if(valores[i]==valores[i+1]):
        pAtual += 1
    if(valores[i]!=valores[i+1]):
        if(pAtual>pMaior):
            pMaior = pAtual
        pAtual = 0
    if(pAtual>pMaior):
            pMaior = pAtual
pMaior+=1
print(pMaior)
