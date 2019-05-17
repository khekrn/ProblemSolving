import collections

def minimumLoss(price):
    n = len(price)
    my_dict = {}
    for index, element in enumerate(price):
        my_dict[element] = index
    nums = sorted(my_dict)    
    index = n - 1
    min_loss = 10**10
    while index > 0:
        if nums[index] - nums[index - 1] < min_loss and my_dict[nums[index]] < my_dict[nums[index - 1]]:
            min_loss = nums[index] - nums[index - 1]
        index -= 1
    return min_loss

price = [5,10,3]
print(minimumLoss(price))

price = [20, 7, 8, 2, 5]
print(minimumLoss(price))


price = [20, 15, 8, 2, 12]
print(minimumLoss(price))
