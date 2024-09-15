def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


def get_min(in_data):
    min = in_data[0]
    for i in range(0, len(in_data)):
        if min > in_data[i]:
            min = in_data[i]
    return min


def get_max(in_data):
    max = in_data[0]
    for i in range(0, len(in_data)):
        if max < in_data[i]:
            max = in_data[i]
    return max


def get_len(in_data):
    return len(in_data)

def get_sum(in_data):
    sum = 0
    for num in in_data:
        sum += num
    return sum

def sorted(in_data):
    out_data = []
    for num in in_data:
        out_data.append(num)
    for index in range(1, len(out_data)):
        out_data[index] = get_max(in_data)
    for index in range(1, len(out_data)):
        for i in range(0, len(in_data)):
            if (out_data[index] > in_data[i]) and out_data[index - 1] < in_data[i]:
                out_data[index] = in_data[i]


    return out_data

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
