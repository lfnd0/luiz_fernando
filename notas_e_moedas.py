valor = float(input())

notas001 = 0
notas005 = 0
notas010 = 0
notas025 = 0
notas050 = 0
notas1 = 0
notas2 = 0
notas5 = 0
notas10 = 0
notas20 = 0
notas50 = 0
notas100 = 0

if (valor>=100):
    notas100 = (valor//100.00)
    valor = (valor%100.00)
if (valor>=50):
    notas50 = (valor//50.00)
    valor = (valor%50.00)
if (valor>=20):
    notas20 = (valor//20.00)
    valor = (valor%20.00)
if (valor>=10):
    notas10 = (valor//10.00)
    valor = (valor%10.00)
if (valor>=5):
    notas5 = (valor//5.00)
    valor = (valor%5.00)
if(valor>=2):
    notas2 = (valor//2.00)
    valor = (valor%2.00)
if(valor>=1):
    notas1 = (valor//1.00)
    valor = (valor%1.00)
if (valor>=0.50):
    notas050 = (valor//0.50)
    valor = (valor%0.50)
if (valor>=0.25):
    notas025 = (valor//0.25)
    valor = (valor%0.25)
if (valor>=0.10):
    notas010 = (valor//0.10)
    valor = (valor%0.10)
if (valor>=0.05):
    notas005 = (valor//0.05)
    valor = (valor%0.05)
if (valor>=0.01):
    notas001 = (valor//0.01)
    valor = (valor%0.01)

print("NOTAS:")

print("{} nota(s) de R$ 100.00".format("%i" %notas100))
print("{} nota(s) de R$ 50.00".format("%i" %notas50))
print("{} nota(s) de R$ 20.00".format("%i" %notas20))
print("{} nota(s) de R$ 10.00".format("%i" %notas10))
print("{} nota(s) de R$ 5.00".format("%i" %notas5))
print("{} nota(s) de R$ 2.00".format("%i" %notas2))

print("MOEDAS:")

print("{} moeda(s) de R$ 1.00".format("%i" %notas1))
print("{} moeda(s) de R$ 0.50".format("%i" %notas050))
print("{} moeda(s) de R$ 0.25".format("%i" %notas025))
print("{} moeda(s) de R$ 0.10".format("%i" %notas010))
print("{} moeda(s) de R$ 0.05".format("%i" %notas005))
print("{} moeda(s) de R$ 0.01".format("%i" %notas001))
