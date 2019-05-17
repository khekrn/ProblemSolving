def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        my_dict = {}
        for index, value in enumerate(nums):        
            element = target - value
            if element in my_dict:
                return [element, value]
            else:
                my_dict[value] = index
        return []

def threeSum(nums: 'List[int]') -> 'List[List[int]]':
    for index, value in enumerate(nums):        
        print(value, ' - ', twoSum(nums[index:], value))

x = [-1, 0, 1, 2, -1, -4]
threeSum(x)
