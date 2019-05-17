'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to
(m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

def merge(nums1, m, nums2, n) -> None:
    num1_index, num2_index = 0, 0
    temp = nums1
    while num1_index < len(nums1) and num2_index < len(nums2):
        if temp[num1_index] > nums2[num2_index]:
            num1_index += 1
        else:
            nums1[num1_index] = nums2[num2_index]
            num2_index += 1
    print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1, len(nums1), nums2, len(nums2))