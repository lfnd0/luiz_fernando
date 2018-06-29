listaA = []
listaB = []
listaI = []

for i in range(3):
	listaA.append(input("Lista A: "))
	sorted(listaA)
for i in range(3):
	listaB.append(input("Lista B: "))
	sorted(listaB)
listaI = sorted(list(set(listaA) & set(listaB)))
if len(listaI)!= 0:
	print(listaI)
else:
	print("Vazio")
