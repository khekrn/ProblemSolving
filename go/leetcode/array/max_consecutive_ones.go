package array

// Given a binary array, find the maximum number of consecutive 1s in this array.

// Example 1:
// Input: [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s.
//     The maximum number of consecutive 1s is 3.
// Note:

// The input array will only contain 0 and 1.
// The length of input array is a positive integer and will not exceed 10,000

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func FindMaxConsecutiveOnes(nums []int) int {
	bestMax, currentMax := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			currentMax++
		} else {
			if currentMax > bestMax {
				bestMax = currentMax
			}
			currentMax = 0
		}
	}
	return max(bestMax, currentMax)
}
