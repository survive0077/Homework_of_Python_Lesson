def profit(poundslist, valuelist, gotvalue, gotitem, able):

    for pounds in range(able + 1):
        largestvalue = gotvalue[pounds - 1]
        newitem = []
        newpounds = 1
        for j in [p for p in poundslist if p <= pounds]:
            if gotvalue[pounds - j] + valuelist[poundslist.index(j)] >= largestvalue and \
                    not (poundslist.index(j) + 1) in gotitem[pounds - j]:
                largestvalue = gotvalue[pounds - j] + valuelist[poundslist.index(j)]
                newitem = [poundslist.index(j) + 1]
                newpounds = j
        gotvalue[pounds] = largestvalue
        gotitem[pounds] = gotitem[pounds - newpounds] + newitem
    return gotitem, gotvalue


poundslist = [2, 3, 4, 5, 9]
valuelist = [3, 4, 8, 8, 10]
gotvalue = [0] * 21
gotitem = [[]] * 21
able = 20
i, v = profit(poundslist, valuelist, gotvalue, gotitem, able)
print(i)
print("The best choice is :", i[20])
