def Pascal(n):
    if n == 0:
        return [1]
    else:
        l = [1]
        for i in range(n - 1):
            l.append(Pascal(n - 1)[i] + Pascal(n - 1)[i + 1])
        l.append(1)
        return l


list = []
n = int(input("Please enter the number of the line: "))
for i in range(n):
    list.append(Pascal(i))
    print(list[i])
