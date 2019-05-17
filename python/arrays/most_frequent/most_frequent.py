def most_frequent(arr):
    max_count = 0
    arr_element = arr[0]
    my_dict = {}
    for element in arr:
        if element in my_dict:
            my_dict[element] = my_dict[element] + 1
        else:
            my_dict[element] = 1
        if my_dict[element] > max_count:
            max_count = my_dict[element]
            arr_element = element
    return arr_element


arr = [1, 3, 1, 3, 2, 1]
print(most_frequent(arr))

arr = [8, 2, 3, 4, 5, 6]
print(most_frequent(arr))

arr = [1, 5, 2, 2, 5, 1, 5, 2]
print(most_frequent(arr))