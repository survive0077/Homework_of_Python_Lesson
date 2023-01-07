import timeit
import matplotlib.pyplot as plt


def binarySearch1(alist, item):  # iterative
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binarySearch2(alist, item):  # recursive
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)


time1 = []
time2 = []
t = range(10000, 1000001, 2000)
for i in t:
    mylist = list(range(i))
    t1 = timeit.Timer("binarySearch1(mylist, 1) ", "from __main__ import binarySearch1, mylist")
    time1.append(t1.timeit(number=10))
    t2 = timeit.Timer("binarySearch2(mylist, 1)", "from __main__ import binarySearch2, mylist")
    time2.append(t2.timeit(number=10))


plt.scatter(t, time1, marker='o', color='blue', s=40, label='iterative')
plt.scatter(t, time2, marker='+', color='red', s=40, label='recursive')
plt.legend(loc='best')
plt.title("Comparison between a sequential search and a binary search on a list of integers")
plt.xlabel('Length / 10^6')
plt.ylabel('Time / ms')
plt.show()
