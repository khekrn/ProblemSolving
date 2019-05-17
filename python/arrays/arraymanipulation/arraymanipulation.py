def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    max_val = 0
    for op in queries:
        start = op[0] - 1
        stop = op[1]
        val = op[2]
        for i in range(start,stop):
            arr[i] += val
            if arr[i] > max_val:
                max_val = arr[i]
    return max_val

def arrayManipulationV2(n, queries):
    max_val = 0
    my_dict = {}
    max_val = 0
    for op in queries:
        start = op[0] - 1
        stop = op[1]
        val = op[2]
        for i in range(start,stop):
            if i in my_dict:
                my_dict[i] = my_dict[i] + val
            else:
                my_dict[i] = val            
            if my_dict[i] > max_val:
                max_val = my_dict[i]
    return max_val

def arrayManipulationV3(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
        print(" For I = ",i," Values = ",arr)
    maxval = 0
    itt = 0
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval

n = 5
queries = [[1,2,100],[2,5,100],[3,4,100]]
#print(arrayManipulation(n, queries))
#print(arrayManipulationV2(n, queries))
print(arrayManipulationV3(n, queries))