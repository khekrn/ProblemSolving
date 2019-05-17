def equalStacks(h1, h2, h3):
    loop = True
    h1_sum = sum(h1)
    h2_sum = sum(h2)
    h3_sum = sum(h3)
    h1_index = 0
    h2_index = 0
    h3_index = 0
    while loop:
        if h1_sum == h2_sum == h3_sum:
            loop = False
            break
        else:
            if len(h1) !=0 and h1_sum > h2_sum or h1_sum > h3_sum:
                h1_sum -= h1[h1_index]
                #del h1[h1_index]
                h1_index += 1
            if len(h2) !=0 and h2_sum > h3_sum or h2_sum > h1_sum:
                h2_sum -= h2[h2_index]
                #del h2[h2_index]
                h2_index += 1
            if len(h3) !=0 and h3_sum > h1_sum or h3_sum > h2_sum:
                h3_sum -= h3[h3_index]
                #del h3[h3_index]
                h3_index += 1
    print(h1_sum)

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

equalStacks(h1, h2, h3)