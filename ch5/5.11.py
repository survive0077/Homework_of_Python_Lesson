def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1                                       #设置循环在列表的最后一个位置
    n = 0                                                          #计数以区分单次冒泡方向
    m = 0                                                          #设置循环在列表的第一个位置
    while passnum > 0 and exchanges:
        exchanges = False
        n = n + 1
        print("m = %d, passnum = %d" % (m, passnum))
        if n % 2 == 1:                                             #奇数次向上冒泡
            for i in range(passnum, m, -1):
                if alist[i - 1] > alist[i]:
                    exchanges = True
                    alist[i - 1], alist[i] = alist[i], alist[i - 1]#奇数次冒泡结束后搜索起始位置后移一位
            m = m + 1                                              #偶数次向上冒泡
            print(alist)
        else:
            for j in range(m, passnum):
                if alist[j] > alist[j + 1]:
                    exchanges = True
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
            passnum = passnum - 1                                  #偶数次冒泡结束后搜索最后一个位置前移一位
            print(alist)


l = [100, 17, 20, 45, 1, 24, 36, 74, 10]
shortBubbleSort(l)
