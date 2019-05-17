package array

// Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

// Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

// You may return any answer array that satisfies this condition.

// Example 1:

// Input: [4,2,5,7]
// Output: [4,5,2,7]
// Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

// Note:

// 2 <= A.length <= 20000
// A.length % 2 == 0
// 0 <= A[i] <= 1000

func sortArrayByParityII(A []int) []int {
	size := len(A)
	for i, j := 0, 1; i < size; i = i + 2 {
		if A[i]&1 == 0 {
			continue
		}
		for A[j]&1 != 0 {
			j = j + 2
		}
		A[i], A[j] = A[j], A[i]
	}

	return A
}

// Fastest
func sortArrayByParityIIV2(A []int) []int {
	size := len(A)
	res := make([]int, size, size)
	start, end := 0, size-1
	for _, item := range A {
		if item&1 == 0 {
			res[start] = item
			start += 2
		} else {
			res[end] = item
			end -= 2
		}
	}
	return res
}
