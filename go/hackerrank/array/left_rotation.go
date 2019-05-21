package array

func leftRotation(arr []int32, k int) []int32 {
	arr = blockSwap(arr, 0, k-1)
	arr = blockSwap(arr, k, len(arr)-1)
	arr = blockSwap(arr, 0, len(arr)-1)

	return arr
}

func leftRotationV2(arr []int32, k int) []int32 {
	for i := 0; i < k; i++ {
		temp := arr[0]
		copy(arr[0:], arr[1:])
		arr[len(arr)-1] = temp
	}
	return arr
}

func blockSwap(arr []int32, start, end int) []int32 {
	var temp int32
	for start < end {
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp

		start++
		end--
	}
	return arr
}
