'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''


def right_rotate(nums, k):
    index = 0
    while index < k:
        tail = nums[len(nums) - 1]
        nums[1:len(nums)] = nums[0:len(nums)-1]
        nums[0] = tail
        index += 1


def right_rotate_v2(nums, k):
    # K will be less than len(nums)
    nums_copy = list(nums)
    k = k % (len(nums))
    nums_copy = nums_copy[-k:] + nums_copy[:-k]
    for i, num in enumerate(nums_copy):
        nums[i] = num


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

right_rotate(nums, k)
print(nums)

nums = [-1, -100, 3, 99]
k = 2

right_rotate(nums, k)
print(nums)
