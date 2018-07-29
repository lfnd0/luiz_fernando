n1, n2 = input().split(" ")
n1 = int(n1)
n2 = int(n2)

bi = False

while n1<=n2:
    if n1%4==0:
        print(n1)
        n1 = n1+4
        bi = True
    elif n1%4==0 and n1%100!=0:
        print(n1)
        n1 = n1+4
        bi = True
    else:
        n1 = n1+1
if (bi==False):
    print("-1")
print("\n")
