import timeit
import matplotlib.pyplot as plt

lst_time = []
dic_time = []
t = range(10000, 1000001, 20000)
for i in t:
    t1 = timeit.Timer("del l[0]", "from __main__ import l")
    t2 = timeit.Timer("del d[0]", "from __main__ import d")
    l = list(range(i))
    lst_time.append(t1.timeit(number=1))
    d = {j: None for j in range(i)}
    dic_time.append(t2.timeit(number=1))

plt.scatter(t, lst_time, marker='+', color='blue', s=40, label='List')
plt.scatter(t, dic_time, marker='o', color='red', s=40, label='Dictionary')
plt.legend(loc='best')
plt.title("Comparison on the performance of the del operator on lists and dictionaries")
plt.xlabel('Length / 10^6')
plt.ylabel('Time / ms')
plt.show()
