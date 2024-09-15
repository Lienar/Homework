# -*- coding: utf-8 -*-

from pprint import pprint

def custom_write(file_name, strings):
    bite = 0
    string_num = 1
    string_dir = {}
    file = open(file_name, mode='a', encoding='utf8')
    for string in strings:
        file.write(f'{string}')
        bite = file.tell() - len(string.encode('utf-8'))
        file.tell()
        file.write(f'\n')
        string_dir[f'({string_num},{bite})'] = string
        string_num += 1
    file.close()
    return string_dir


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
    print(f'({elem[0]}, {elem[1]})')