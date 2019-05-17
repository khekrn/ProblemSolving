def left_rotate(a, d):
    index = 0
    while index < d:
        element = a.pop(0)
        a.append(element)
        index += 1
    return a

d = 2
a = [1, 2, 3, 4, 5]
print(left_rotate(a, d))

d = 4
a = [1, 2, 3, 4, 5]
print(left_rotate(a, d))