def mergeSort(alist, first, last):
    if (last - first) > 0:
        mid = (last + first + 1) // 2

        a = mergeSort(alist, first, mid - 1)
        b = mergeSort(alist, mid, last)

        i = 0
        j = 0
        c = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1

        while i < len(a):
            c.append(a[i])
            i = i + 1

        while j < len(b):
            c.append(b[j])
            j = j + 1

        return c
    else:
        return [alist[first]]


l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(mergeSort(l, 0, len(l) - 1))
