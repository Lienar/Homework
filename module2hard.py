import random
def result(n):
    password = ''
    for i in range (1, 21):
        for j in range (i, 21):
            if i != n and j != n:
                if n % (i+j) == 0:
                    if i != j:
                        password = password + str(i) + str(j)
    return password

n = random.randint (3, 20)
print (n, '-',result(n))