import numpy as np
import pandas as pd
import numpy
import matplotlib
import matplotlib.pyplot as plt
import random

def data_create_line_array(a1, a2):
    a_all_line=np.hstack((a1, a2))
    return (a_all_line)


def data_create_doble_array(a1, a2):
    a_all_line=np.vstack((a1, a2))
    return (a_all_line)

def data_create_std(a):
    s = float(a.std())
    mi = float(a.min())
    ma = float(a.max())

    return (mi, s, ma)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

b = data_create_line_array(array1, array2)
c = data_create_doble_array(array1, array2)
d = data_create_std(b)

data_f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(data_f)):
    data_f[i] = [(random.randint(100, 500)),  (random.randint(50, 200))]

df = pd.DataFrame(data_f)

print (df)
df.mean()

df.plot()
plt.show()

df.to_csv("data1.csv")

x = 0
y = 0

data_x = [(0,0), (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0), (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

for x in range(-30, 30):
    y = (x*x) * 100
    z = (x*x*x) * 50
    data_x[x+30] = (x, z, y)

graf = plt.plot(data_x)


plt.show()

g = data_create_line_array(array1, array2)

plt.bar(array1, array2)
plt.show()








