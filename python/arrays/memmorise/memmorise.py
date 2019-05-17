from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
table = Counter(arr)
Q = int(input)
for i in range(Q):
    x = int(input())
    if x in table:
        print(table[x])
    else:
        print("NOT PRESENT")