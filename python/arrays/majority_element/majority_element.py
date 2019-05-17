'''
Given an array of size n, find the majority element. The majority element is 
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''
def majorityElement(nums) -> int:
    majority_count = int(len(nums) / 2)
    my_dict = {}
    res = None
    for element in nums:
        element_count = 1
        if element in my_dict:
            element_count = my_dict[element] + 1
            my_dict[element] = element_count
        else:
            my_dict[element] = 1
        if element_count > majority_count:
            res = element
            break
    return res


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([1]))