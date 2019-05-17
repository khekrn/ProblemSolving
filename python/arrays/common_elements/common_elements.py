def common_elements(A, B): 
    res = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
    return res

A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

print(common_elements(A, B))

A = [1, 3, 4, 4, 6, 7, 9]
B = [1, 2, 4, 5, 6, 9, 10]

print(common_elements(A, B))