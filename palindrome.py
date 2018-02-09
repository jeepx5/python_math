def palindrome(x):

    s=1 if x >0 else -1
    x=x*s
    strx=str(x)
    rst=int((strx[0:])[::-1])
    print(rst)
    rst = rst * s * (rst < 0x7FFFFFFF)

    return x==rst





def main():
    print('start main')
    print(palindrome(-15342469))
    print('end main')

if __name__ == '__main__':
	main()
