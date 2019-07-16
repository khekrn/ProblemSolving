package hackerrank

// HourglassSum function
func HourglassSum(arr [][]int32) int32 {
	var max int32
	rows := len(arr)
	cols := len(arr[0])
	startRow, midRow, stopRow := 0, 1, 2
	for startRow < rows && stopRow < rows {
		startIndex, midIndex, stopIndex := 0, 1, 3
		for startIndex < cols && stopIndex <= cols {
			head := arr[startRow][startIndex:stopIndex]
			mid := arr[midRow][midIndex]
			tail := arr[stopRow][startIndex:stopIndex]
			currentMax := sum(head) + mid + sum(tail)
			if currentMax > max {
				max = currentMax
			}
			startIndex, midIndex, stopIndex = startIndex+1, midIndex+1, stopIndex+1
		}
		startRow, midRow, stopRow = startRow+1, midRow+1, stopRow+1
	}

	return max
}

func sum(arr []int32) int32 {
	var res int32
	for _, item := range arr {
		res += item
	}
	return res
}
