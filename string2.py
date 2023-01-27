# string2 assignment

def verbing(s):
    if len(s) >= 3:
        if s[-3:] != 'ing': s = s + 'ing'
        else: s = s + 'ly'
    return(s)

def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if n != -1 and b != -1 and b > n:
        s = s[:n] + 'good' + s[b+3:]
    return s

def test(got, expected):
    if got == expected:
        prefix = 'OK'
    else:
        prefix = 'X'
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('verbing')

    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')

    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This tea is not hot'), 'This tea is not hot')



if __name__ == '__main__':
    main()
