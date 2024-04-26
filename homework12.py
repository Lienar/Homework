def test(*params):
    print(params)

test(1, 2, 3, 'Go')

data = [1, 5, 6, '7', 'No', 9]

def factoril(*data):
    n = 0
    t = ' '
    res = 1
    for i in data:
        if type(i) == type(n):
            n += i
        if type(i) == type(t):
            t += i
            t += ' '

    return n

def factoril_of_N(n):
    if n == 0:
        return 1
    else:
        return n*factoril_of_N(n-1)

s = factoril(*data)

print (factoril_of_N(s))

