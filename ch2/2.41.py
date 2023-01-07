import timeit
import matplotlib.pyplot as plt
# O(nlogn)

def partition(nums=list):
    pivot = nums[0]
    small = [x for x in nums[1:] if x < pivot]
    large = [x for x in nums[1:] if x >= pivot]
    return small, pivot, large


def quick_sort(nums=list):
    if len(nums) <= 1:
        return nums
    small, pivot, large = partition(nums)
    return quick_sort(small) + [pivot] + quick_sort(large)


lis = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
l = quick_sort(lis)
k = int(input("Please enter the kth smallest number you want to find."))
print(l)
print("The kth smallest number is ", l[k])

'''lst_time = []
t = range(10, 1000, 200)
for i in t:
    t = timeit.Timer("quick_sort(l)", "from __main__ import l,quick_sort,partition")
    l = list(range(i))
    lst_time.append(t.timeit(number=100))

plt.plot(lst_time)
plt.show()'''

