import timeit
import matplotlib.pyplot as plt
# O(n)
'''使用桶排序法，先调用列表函数找到最大和最小值，max,min函数时间复杂度都为O(n),之后建立一个包含max-min个桶的列表，然后遍历一次输入数组，相应的数字放入
对应桶中，结束后遍历一遍桶列表，输出对应元素即完成排序，两次遍历时间复杂度为O(M+n),故总时间复杂度为O(n)'''
def bucket_sort(lst):
    Max, Min = max(lst), min(lst)
    buckets = [0] * ((Max - Min)+1)
    for i in range(len(lst)):
        buckets[lst[i]-Min] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+Min]*buckets[i]
    return res


lis = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
l = bucket_sort(lis)
k = int(input("Please enter the kth smallest number you want to find."))
print(l)
print("The kth smallest number is ", l[k])
