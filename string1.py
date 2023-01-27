# string1 assignment

def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

def both_ends(s):
    if len(s) < 2:
        return ''
    first_two = s[0:2]
    last_two = s[-2:]
    return first_two + last_two

def fix_start(s):
    front = s[0]
    back = s[1:]
    fixed_back = back.replace(front, '*')
    return front + fixed_back

def test(got, expected):
    if got == expected:
        prefix = 'OK'
    else:
        prefix = 'X'
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('donuts')

    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(55), 'Number of donuts: many')

    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('google'), 'gole')
    test(both_ends('a'), '')

    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')



if __name__ == '__main__':
    main()
