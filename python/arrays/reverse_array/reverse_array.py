def reverseArray(a):
    res = []
    index = len(a)-1
    while index >= 0:
        res.append(a[index])
        index -= 1
    return res

print(reverseArray([1, 2, 3, 4, 5]))