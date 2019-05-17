'''
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


def searchInsert(nums: 'List[int]', target: 'int') -> 'int':
    low = 0
    high = len(nums) - 1
    mid = low + int((high - low) / 2)
    if nums[mid] < target:
        return search(nums, target, mid, len(nums))
    elif nums[mid] > target:
        return search(nums, target, 0, mid)        
    else:
        return mid
    return 0

def search(nums: 'List[int]', target: 'int', index: 'int', size: 'int') -> 'int':    
    while index < len(nums):
        if nums[index] < target:
            index += 1
        else:
            break
    return index


x = [1,3,5,6]
print(searchInsert(x, 5))

x = [1,3,5,6]
print(searchInsert(x, 2))

x = [1,3,5,6]
print(searchInsert(x, 7))

x = [1,3,5,6]
print(searchInsert(x, 0))