lista_ano = []
lista_vel = []
vel_media = 0

verifica = str(input())

if (verifica == "n"):
    print("Zero")

else:
    
    while (verifica == "s"):
        ano = int(input())
        lista_ano.append(ano)
        vel = float(input())
        lista_vel.append(vel)
        verifica = str(input())
        vel_media = (vel_media + vel)

    if (verifica == "n"):
        vel_media = vel_media / len(lista_vel)
        print("%.2f" %max(lista_vel))
        print(max(lista_ano))
        print("%.2f" %vel_media)
