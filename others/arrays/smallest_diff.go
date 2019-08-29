package arrays

// Finding out the minimum absolute difference between elements in an array

// Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
// Sample output: [28, 26]

import (
	"math"
	"sort"
)

// MinimumDifference Finding out the minimum absolute difference
func MinimumDifference(arr1, arr2 []int32) []int32 {
	sort.Slice(arr1, func(i int, j int) bool { return arr1[i] < arr1[j] })
	sort.Slice(arr2, func(i int, j int) bool { return arr2[i] < arr2[j] })

	indexOne, indexTwo := 0, 0
	var minValue int32 = math.MaxInt32
	var currentMinValue int32 = math.MaxInt32

	res := []int32{0, 0}
	for indexOne < len(arr1) && indexTwo < len(arr2) {
		first, second := arr1[indexOne], arr2[indexTwo]
		if first < second {
			currentMinValue = second - first
			indexOne++
		} else if first > second {
			currentMinValue = first - second
			indexTwo++
		} else {
			res[0], res[1] = first, second
			break
		}
		if currentMinValue < minValue {
			minValue = currentMinValue
			res[0], res[1] = first, second
		}
	}

	return res
}
