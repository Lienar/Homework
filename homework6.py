Privet = 'Здравствуйте!'
Poka = 'До свидания'
Result = 'Успех'


print('Задание 1')

x = 38
print(Privet)

if x < 0:
    print('Меньше нуля')

print(Poka)

print('')
print('')
print('')
print('Задание 2')

print(Privet)

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('a > b and a > 0', Result)

if (a > b) and (a > 0 or b < 1000):
    print('(a > b) and (a > 0 or b < 1000)', Result)

if (5 < b) and (b < 10):
    print('5 < b and b < 10', Result)

print(Poka)

print('')
print('')
print('')
print('Задание 3')

print(Privet)

if '34' > '123':
    print("'34' > '123'",Result)

if '123' > '12':
    print("'123' > '12'", Result)

if [1, 2] > [1, 1]:
    print('[1, 2] > [1, 1]', Result)

print(Poka)

print('')
print('')
print('')
print('')
print('Задание 4')

print(Privet)

if '6' > 5:
    print("'6' > 5",Result)

if [5, 6] > 5:
    print('[5, 6] > 5',Result)

if '6' > 5:
    print("'6' > 5", Result)

print(Poka)