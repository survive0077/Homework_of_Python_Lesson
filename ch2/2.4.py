
import timeit
import matplotlib.pyplot as plt


def partition(nums=list):
    a = nums[0]
    small = [x for x in nums[1:] if x < a]
    lagre = [x for x in nums[1:] if x >= a]
    return small, a, lagre


def solve(nums, key):
    small, a, lagre = partition(nums)
    n = len(small)
    if n == key:
        return a
    elif n < key:
        return solve(lagre, key-n-1)
    else:
        return solve(small, key)


lst_time = []
t = range(100, 1001, 20)
for i in t:
    t = timeit.Timer("solve(l, 4)", "from __main__ import l,solve,partition")
    l = list(range(i))
    lst_time.append(t.timeit(number=100))

plt.plot(lst_time)
plt.show()