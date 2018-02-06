def reverse(x):
    sx=(x)>0
    s=(sx*2-1)
    x=x*s
    rst = 0
    msb = 0
    leng = len(str(x))
    strx=str(x)
    print((strx[1:])[::-1])
    lst=range(leng,1,1)
    for i in range(leng,0,-1):
        msb = int(x%10**(i) / 10 ** (i-1))
        rst = rst + msb * 10 ** (leng - i)
    print('reverse done')

    return rst*s*(rst<0x7FFFFFFF)

def reverse2(x):

    s=1 if x >0 else -1
    x=x*s
    strx=str(x)
    rst=int((strx[0:])[::-1])
    print(rst)
    return rst*s*(rst<0x7FFFFFFF)

def main():
    print('start main')
    print(reverse2(-15342469))
    print('end main')

if __name__ == '__main__':
	main()
