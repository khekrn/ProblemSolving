'''
Given 

Index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Chars = [a, b, c, d, e, f, g, h, i]

Position 2 is a peak if and only if b ≥ a and b ≥ c. Position 9 is a peak if i ≥ h.
'''


def find_peak(arr):
    '''
    O(log n)
    '''

    size = len(arr)

    if size == 1 or arr[0] > arr[1]:
        return 0
    
    if arr[size-1] > arr[size-2]:
        return size-1
    
    def peak_finder(elements, low, high):
        if low == high:
            return low
        
        mid = int((low + high) / 2)
        if elements[mid] > elements[mid + 1]:
            return peak_finder(elements, low, mid)
        return peak_finder(elements, mid+1, high)

    return peak_finder(arr, 0, len(arr)-1)


def find_peak_v1(arr):
    '''
    O(n)
    '''
    size = len(arr)

    if size == 0 or size == 1:
        return 0

    if arr[0] > arr[1]:
        return 0

    if arr[size-1] > arr[size-2]:
        return size-1

    i = 1
    while i <= size-2:
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            return i
        i += 1
    return -1


arr = [1, 2, 3, 1]
print(find_peak(arr))

arr = [1, 2, 1, 2, 1]
print(find_peak(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_peak(arr))

arr = [10, 2, 3, 4, 2, 1, 2, 3]
print(find_peak(arr))

arr = [1, 2, 3, 4, 2, 1, 8, 3]
print(find_peak(arr))


'''

arr = [1, 2, 3, 1]
print(find_peak_v1(arr))

arr = [1,2,1,2,1]
print(find_peak_v1(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_peak_v1(arr))

arr = [10, 2, 3, 4, 2, 1, 2, 3]
print(find_peak_v1(arr))

arr = [1, 2, 3, 4, 2, 1, 8, 3]
print(find_peak_v1(arr))
'''
