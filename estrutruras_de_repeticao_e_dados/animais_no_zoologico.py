def cadastrar(tipo, peso, pais):
    animal = [tipo, peso, pais]
    return animal

continuar = True
parar = ''
tipo = ''
peso = 0.0
pais = ''
zoo = {}
aux = []
cont = 0

while continuar:
    tipo = str(input().lower())
    peso = float(input())
    pais = input().capitalize()
    parar = str(input().lower())
    zoo[cont] = cadastrar(tipo, peso, pais)
    aux = []
    cont += 1
    if parar == 'parar':
        break
    elif parar == 'continuar':
        pass

n_macacos = v_cobras = n_tigres = 0
peso_tigres = 0.0

for x in range(cont):
    if zoo[x][0] == 'macaco':
        n_macacos += 1
    elif zoo[x][0] == 'tigre':
        peso_tigres += zoo[x][1]
        n_tigres += 1
    elif zoo[x][0] == 'cobra' and zoo[x][2] == 'Venezuela':
        v_cobras += 1

if n_tigres == 0:
    peso_tigres = 0
else:
    peso_tigres /= n_tigres

print(n_macacos)
print('{:.2f}'.format(peso_tigres))
print(v_cobras)
