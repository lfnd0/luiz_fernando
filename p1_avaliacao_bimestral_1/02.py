def tabuada_mul(k, l, m):
    while(k <= 9) and (l <= 10):
        print('%d*%d=%d' %(k, l, m))
        l = l+1
        if (l==11):
            k = k + 1
            l = 1
        m = k * l
        tabuada_mul(k, l, m)
        break

res = tabuada_mul(1, 1, 1)
