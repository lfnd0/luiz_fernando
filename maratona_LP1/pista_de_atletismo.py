n = input()
c = list(map(int,n.split(' ')))
n1 = c[0]
n2 = c[1]
inicio = n1
while(n2<=n1):
    if(n1-n2>=0):
        n1-=n2
print(n1)
