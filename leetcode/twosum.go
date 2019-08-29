package leetcode

import "sort"

// TwoNumberSum Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
// If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
// If no two numbers sum up to the target sum, the function should return an empty array.
// Assume that there will be at most one pair of numbers summing up to the target sum.
// O(n) && Space is also O(n)
func TwoNumberSum(array []int, target int) []int {
	dict := make(map[int]struct{})
	var nothing struct{}
	for _, item := range array {
		sumElement := target - item
		if _, found := dict[sumElement]; found {
			res := []int{0, 0}
			if item < sumElement {
				res[0], res[1] = item, sumElement
			} else {
				res[0], res[1] = sumElement, item
			}
			return res
		} else {
			dict[item] = nothing
		}
	}

	return []int{}
}

// TwoNumberSumV2 Time - O(n * log n) and Space O(1)
func TwoNumberSumV2(array []int, target int) []int {
	sort.Ints(array)

	left, right := 0, len(array)-1

	for left < right {
		sumElement := array[left] + array[right]

		if sumElement == target {
			return []int{array[left], array[right]}
		} else if sumElement < target {
			left++
		} else {
			right--
		}
	}

	return []int{}
}
