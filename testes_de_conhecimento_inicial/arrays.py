nA = int(input())
nB = int(input())
kA = int(input())
mB = int(input())
listaA = []
listaB = []
sub_listaA = []
sub_listaB = []

for i in range(nA):
	listaA.append(input())
for i in range(nB):
	listaB.append(input())

sub_listaA = [1, kA]
sub_listaB = [1, mB]

if (sub_listaA > sub_listaB):
	print("Sim")
else:
	print("Não")
