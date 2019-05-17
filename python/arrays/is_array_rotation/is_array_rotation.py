def is_rotation(A, B):
    if len(A) is not len(B):
        return False
    i, j = 0, 0
    while j < len(B):
        if B[j] == A[i]:
            break
        else:
            j += 1
    if j == len(B):
        return False
    while i < len(B):
        if A[i] == B[j]:
            i += 1
            j += 1
            if j >= len(B):
                j = 0
        else:
            return False
    return True

A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]

print(is_rotation(A, B))

A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 1]

print(is_rotation(A, B))

A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2]

print(is_rotation(A, B))


A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 0, 2, 3]

print(is_rotation(A, B))