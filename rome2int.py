def rometoint(s):
    """
           :type s: str
           :rtype: int
           Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
           I, II, III, IIII, V, VI, VII, VIII, VIIII, X.
           X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.
           C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.
           """


    rn = {}
    rn['M'] = 1000
    rn['D'] = 500
    rn['C'] = 100
    rn['L'] = 50
    rn['X'] = 10
    rn['V'] = 5
    rn['I'] = 1
    tmp = s[0]
    rst = 0
    i = 0
    while i <= len(s) - 2:
        # print('====', rst, i, tmp)
        if rn[s[i]] >= rn[s[i+1]]:
            rst += rn[s[i]]
            i+=1
        else:
            rst -= rn[s[i]]
            i+=1
    rst+=rn[s[i]]
    return rst


def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]


def main():
    print('start main')
    print(rometoint("DCXXI"), romanToInt("DCXXI"))
    print(rometoint("MCMXCVI"), romanToInt("MCMXCVI"))
    print(rometoint("MDCCCLXXXIV"), romanToInt("MDCCCLXXXIV"))
    print(rometoint("MDLXX"), romanToInt("MDLXX"))
    print(rometoint("MCDLXXVI"), romanToInt("MCDLXXVI"))
    print(rometoint("MMCCCXCIX"), romanToInt("MMCCCXCIX"))
    print('end main')

if __name__ == '__main__':
	main()
