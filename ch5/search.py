def sort(list, n):
    found = False
    if list[0] == n:
        found = True
    elif len(list) > 1:
        found = found or sort(list[1:], n)
    else:
        found = False
    return found


l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
print(sort(l, 31))
print(sort(l, 10))
