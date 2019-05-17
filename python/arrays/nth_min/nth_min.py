def find_nth_min(arr, num):
    return nth_min(arr, num-1)

def nth_min(arr, num):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if num < num_less:
        return nth_min(below, num)
    elif num >= num_lessoreq:
        return nth_min(above, num-num_lessoreq)
    else:
        return pivot

arr = [4, 9, 3, 15, 11]
print(find_nth_min(arr, 4))
