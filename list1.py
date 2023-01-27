# List1 assignment program

def match_ends(words):
    count = 0
    for item in words:
        if (len(item) >= 2) and (item[0] == item[-1]):
            count += 1
    return count
            
def front_x(words):
    l1 = list()
    l2 = list()
    for item in words:
        if item[0] == 'x':
            l1.append(item)
            print('if loop', l1)
        else:
            l2.append(item)
            print('else loop', l2)
    return l1+l2
    
        
def test(got, expected):
    if got == expected:
        prefix = 'OK'
    else:
        prefix = 'X'
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


#Calls the above the functions with intersting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])


if __name__ == '__main__':
    main()
