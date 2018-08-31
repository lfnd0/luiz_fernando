acabou = False
partidas = int(input())
j = 0
while(j < partidas):
    while(acabou == False):
        senha = 0
        chute = 0
        quant = int(input())
        i = 0
        senha = input()
        while(i<quant):
            chute = input()
            aux = 0
            excelente = 0
            bom = 0
            while(aux<len(senha)):
                if(senha[aux]==chute[aux]):
                    excelente += 1
                else:
                    aux2 = 0
                    while(aux2<len(senha)):
                        if(chute[aux2]==senha[aux]):
                            bom+=1
                            break
                        aux2+=1
                aux+=1
            print("(%i,%i)"%(excelente,bom))
            if(excelente == len(senha)):
                acabou = True
            i+=1
    acabou = False
    j+=1
