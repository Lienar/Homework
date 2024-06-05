
def add_everything_up(a, b):
    summ = ''
    try:
        if (type(a) == str) and (type(b) == int or type(b) == float):
            b = str(b)
            summ = a + b

        if (type(b) == str) and (type(a) == int or type(a) == float):
            a = str(a)
            summ = a + b

        if (type(a) == type(b)) or (type(a) == int and type(b) == float)  or (type(b) == int and type(a) == float):
            summ = int('gf')

    except:
        summ = a + b

    return (summ)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))