n1 = int(input())
i = 1
t = 0

while (t < n1):
    t = i*(i+1)*(i+2)
    i += 1

if (t == n1 and n1 != 0):
    print (i-1,"*",(i),"*",(i+1), "=", n1)
    print ("Verdadeiro")

else: 
    print ("Falso")
