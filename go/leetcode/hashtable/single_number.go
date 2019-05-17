package hashtable

// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note:

// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1:

// Input: [2,2,1]
// Output: 1
// Example 2:

// Input: [4,1,2,1,2]
// Output: 4

func SingleNumber(nums []int) int {
	dict := make(map[int]struct{})
	var empty struct{}
	for i := 0; i < len(nums); i++ {
		if _, exist := dict[nums[i]]; exist {
			delete(dict, nums[i])
		} else {
			dict[nums[i]] = empty
		}
	}
	var res int
	for key := range dict {
		res = key
	}
	return res
}
