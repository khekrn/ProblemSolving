def missing_numberV1(arr, brr):
    arr.sort()
    brr.sort()    
    res = set()
    a_size = len(arr)
    b_size = len(brr)
    a_index = 0
    b_index = 0
    while b_index < b_size:
        while a_index < a_size and arr[a_index] == brr[b_index]:
            a_index += 1
            b_index += 1
        res.add(brr[b_index])
        b_index += 1    
    return sorted(res)

def missing_numberV2(arr, brr):
    brr.sort()
    res = set()
    for element in brr:
        if brr.count(element) > arr.count(element):
            res.add(element)
    return sorted(res)


arr = [203,204,205,206,207,208,203,204,205,206]
brr = [203,204,204,205,206,207,205,208,203,206,205,206,204]
print(missing_numberV1(arr, brr))
print(missing_numberV2(arr, brr))

arr = [203,204,205,206,207,208,203,204,205,206]
brr = [203,204,204,205,206,207,205,208,203,206,205,206,204, 209]
print(missing_numberV1(arr, brr))
print(missing_numberV2(arr, brr))