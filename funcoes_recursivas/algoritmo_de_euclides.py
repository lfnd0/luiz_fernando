import math
def mdc(quant):
    if(quant>0):
        valor = input()
        valor1 = valor
        valor = valor.split(' ')
        try:
            entrada = list(map(int,valor))
        except ValueError:
            valor1 = valor1.split(chr(9))
            entrada = list(map(int,valor1))
        a = entrada[0]
        d = entrada[1]
        if(a%d == 0):
            print("MDC(%i,%i) = %i"%(a,d,d))
        else:
            while(1==1):
                resto = (a%d)
                resto = math.floor(resto)
                if(a%d == 0):
                    print("MDC(%i,%i) = %i"%(entrada[0],entrada[1],d))
                    break
                a = d
                d = resto
        entrada.clear()
        mdc(quant-1)
n = int(input())
mdc(n)
