listaA = []
listaB = []
listaI = []

for i in range(20):
	listaA.append(input())
	sorted(listaA)
for i in range(20):
	listaB.append(input())
	sorted(listaB)
listaI = sorted(list(set(listaA) & set(listaB)))
if len(listaI)!= 0:
	print(listaI)
else:
	print("Vazio")
