def pairs(k, arr):
    arr.sort()
    num_set = set()
    pair_res = 0
    for element in arr:
        if (element - k) in num_set:
            pair_res += 1
        num_set.add(element)
    return pair_res

k = 1
arr = [1, 2, 3, 4]
print(pairs(k, arr))