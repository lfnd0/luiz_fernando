n1, n2 = input().split(" ")
n1 = int(n1)
n2 = int(n2)

bi = 0

while n1<=n2:
    if n1%4==0:
        print(n1)
        n1 = n1+4
        bi = 1
    elif n1%4==0 and n1%100!=0:
        print(n1)
        n1 = n1+4
        bi = 1
    else:
        n1 = n1+1
if (bi==0):
    print("-1")
print("\n")
