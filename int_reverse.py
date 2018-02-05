def reverse(x):
    sx=(x)>0
    s=sx*2-1
    x=x*s
    rst = 0
    msb = 0
    leng = len(str(x))
    lst=range(leng,1,1)
    for i in range(leng,0,-1):
        print(i)
        msb = int(x%10**(i) / 10 ** (i-1))
        print('==>',msb)

        rst = rst + msb * 10 ** (leng - i)
    print('reverse done')

    return rst*s
