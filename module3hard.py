data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structue_sum(*args):
    data_structure_in = [*args[0]]
    summa = 0
    for i in range(len(data_structure_in)):
        if (type(data_structure_in[i])) == float or (type(data_structure_in[i])) == int:
            summa += data_structure_in[i]
        if (type(data_structure_in[i])) == str:
            summa += len(data_structure_in[i])
        if (type(data_structure_in[i])) == tuple or (type(data_structure_in[i])) == list:
            summa += calculate_structue_sum(data_structure_in[i])
        if ((type(data_structure_in[i])) == dict):
            summa += (calculate_structue_sum(list(dict.values(data_structure_in[i]))))
            summa += (calculate_structue_sum(list(dict.keys(data_structure_in[i]))))
        if ((type(data_structure_in[i])) == set):
           summa += calculate_structue_sum(list(data_structure_in[i]))
    return summa

print (calculate_structue_sum(data_structure))

