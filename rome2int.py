def rometoint(s):
    """
           :type s: str
           :rtype: int
           Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
           I, II, III, IIII, V, VI, VII, VIII, VIIII, X.
           X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.
           C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.
           """

    rn={}
    rn['M']=1000
    rn['D'] = 500
    rn['C'] = 100
    rn['L']=50
    rn['X']=10
    rn['V']=5
    rn['I']=1
    tmp=s[0]
    rst=0
    i=1
    while i <= len(s)-1:
        tmp = rn[s[i-1]]
        print(i, tmp, rst)
        if tmp==1000:
            rst+=tmp
            i+=1
            continue
        if rn[s[i]] > tmp:
            rst = rst+rn[s[i]]-tmp
            i+=2
            continue
        elif rn[s[i]] == tmp :
            rst =rst+tmp+tmp
            if i == len(s)-2:
                i+=1
                rst -= tmp
            else:
                i+=2

            continue
        elif rn[s[i]] < tmp:
            rst = rst + rn[s[i]] + tmp
            i+=2
        #print(i, rst)
        if i == len(s):
            rst +=rn[s[-1]]

    return rst


def main():
    print('start main')
    print(rometoint("DCXXI"))
    print(rometoint("MCMXCVI"))
    print(rometoint("MDCCCLXXXIV"))
    print(rometoint("MDLXX"))
    print(rometoint("MCDLXXVI"))
    print('end main')

if __name__ == '__main__':
	main()
