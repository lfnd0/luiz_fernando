def search(lista, busca):
    nomes_encontrados = []
    for x in lista:
        if busca in x.lower():
            nomes_encontrados.append(x)
    return nomes_encontrados

nomes = []
nome = ''

for x in range(10):

    nome = input()
    nomes.append(nome)
buscar = input().lower()

result_pesquisa = search(nomes, buscar)

for x in result_pesquisa:
    print(x)
