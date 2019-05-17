def maxSubArray(nums: 'List[int]') -> 'int':
    if not nums:
        return 0
    max_sum = nums[0]
    start = 1
    while start < len(nums):
        i = 0
        while i < start:
            temp = sum(nums[i:start])            
            if temp > max_sum:
                max_sum = temp
            i += 1
        start += 1
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))