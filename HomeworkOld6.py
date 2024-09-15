first = 'Мама мыла раму'
second = 'Рамена мало было'

result =map(lambda x,y: x == y, first, second)
print (list(result))

def get_advanced_writer(file_name):
    file = open(file_name, mode='a', encoding='utf8')
    def  write_everything(*data_set):
        for data in data_set:
            file.write(f'{data} \n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random

class MysticBall:

    def __init__(self, *word):
        self.words = word

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())