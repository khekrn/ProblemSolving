def matchingStrings(strings, queries):
    my_dict = {}
    for item in strings:
        if item in my_dict:
            my_dict[item] = my_dict[item] + 1
        else:
            my_dict[item] = 1
    res = []
    for item in queries:
        if item in my_dict:
            res.append(my_dict[item])
        else:
            res.append(0)
    return res

strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

print(matchingStrings(strings, queries))