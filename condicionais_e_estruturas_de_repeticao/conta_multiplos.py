n1 = int(input())
n2 = int(input())

i = 1
cont = 0

while i<50:
    if i%n1==0 and i%n2==0:
        cont = cont+1
    i = i + 1

print(cont)
