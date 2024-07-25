import requests
import inspect

answer = ['Name', 'Type','Attributes and methods', 'Module', 'Source', 'Object length', 'Isiterable']
s = ''

def introspection_info(obj):
    answer_in = ['', '',[], '', '', '', '']
    try:
        answer_in[0] = obj.__name__
    except:
        answer_in[0] = 'None'

    answer_in[1] = type(obj)

    answer_in[2] = dir(obj)

    try:
        answer_in[3] = obj.__module__
    except:
        answer_in[3] = 'main'

    try:
        answer_in[4] = inspect.findsource(obj)
    except:
        answer_in[4] = 'None'

    try:
        answer_in[5] = len(obj)
    except:
        answer_in[5] = '1'

    try:
        iter(obj)
        answer_in[6] = 'Yes'
    except:
        answer_in[6] = 'Not'

    return answer_in

answer_out = introspection_info(12)

for i in range (0, len(answer_out)):
    print(answer[i], ' = ', answer_out[i])





