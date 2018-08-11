entrada = input()
entrada = entrada.split(' ')
entrada = list(map(str, entrada))
p1 = entrada[0]
p2 = entrada[1]
criptografia = ''
aux = 0   
if(len(p1) == len(p2) and ((p1.islower()== True) or (p1.isdigit())) and ((p2.islower()== True) or (p2.isdigit()))):
    for i in p1:
        if((i == p2[aux]) and (i != 'a') and (i != 'e') and (i != 'i') and (i != 'o') and (i != 'u')):
            criptografia += str(aux)        
        elif(aux%2==0):
            criptografia += i.upper()
        else:
            criptografia += '!!'
        aux+=1
    print(criptografia)
else:
    print("ERRO")
