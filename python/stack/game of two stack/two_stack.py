def twoStacks(x, a, b):
    a_list, b_list = [], []
    pops_list = []
    a_sum, b_sum = 0, 0
    a_index, b_index = 0, 0

    while a_index < len(a):
        if a_sum + a[a_index] <= x:
            a_list.append(a[a_index])
            a_sum += a[a_index]
        else:
            break
        a_index += 1
    
    while b_index < len(b):
        if b_sum + b[b_index] <= x:
            b_list.append(b[b_index])
            b_sum += b[b_index]
        else:
            break
        b_index += 1
    pops_list.append(len(a_list))
    pops_list.append(len(b_list))

    index, sum_val = 0, 0
    pop_count = 0
    loop = True

    while loop:
        a_element, b_element = None, None
        if index < len(a_list):
            a_element = a_list[index]
        if index < len(b_list):
            b_element = b_list[index]

        if a_element is not None and sum_val + a_element <= x:
            pop_count += 1
            sum_val += a_element

        if b_element is not None and sum_val + b_element <= x:
            pop_count += 1
            sum_val += b_element
        index += 1
        if index >= len(a_list) and index >= len(b_list):
            break

    pops_list.append(pop_count)
    return max(pops_list)

def twoStacksV2(x, a, b):
    y = []
    a.reverse()
    b.reverse()
    
    c = []
    m_num = 0
    s1 = 0
    
    while a != []:
        if s1 + a[-1] <= x:
            c.append(a.pop())
            s1 += c[-1]
            m_num += 1
        else:
            break
    
    s2 = 0
    
    while b != []:
        if s2 + b[-1] <= x:
            if s1 + b[-1] <= x:
                el = b.pop()
                s1 += el
                s2 += el
                m_num += 1
            else:
                el = b.pop()
                s1 += el - c.pop()
                s2 += el
        else:
            break
    if sum(y) > x:
        y.pop()
    return m_num

x = 10
a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
print(twoStacks(x, a, b))
print(twoStacksV2(x, a, b))


a = [7, 15, 12, 0, 5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16]
b = [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 1]
x = 67
print(twoStacks(x, a, b))

print(twoStacksV2(x, a, b))