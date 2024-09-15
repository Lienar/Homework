def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    try:
        for num in numbers:
            try:
                result += num
            except:
                incorrect_data += 1
    except:
        incorrect_data += 1
    result_dir = [result, incorrect_data]
    return result_dir


def calculate_averaga(numbers):
    num_num = 0
    try:
        for num in numbers:
            if (type(num) == int) or (type(num) == float):
                num_num += 1
            else:
                print(f'Некорректный тип данных для подсчёта суммы {type(num)} {num}')
    except:
        print('В numbers записан некорректный тип данных')
        return 'None'
    summ = personal_sum(numbers)
    try:
        result = summ[0]/num_num
    except ZeroDivisionError:
        result = 0
    return result


data = ["1, 2, 3", [1, "Строка", 3, "Ещё Строка"], 567, [42, 15, 36, 13]]

index = 1
for i in data:
    print(f'Результат {index}: {calculate_averaga(i)}')
    index +=1
    
