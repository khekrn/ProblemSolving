package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello Go!!")

	arr := []int32{1, 2, 3, 4}
	fmt.Println(ReverseArray(arr))
}

func ReverseArray(arr []int32) []int32 {
	size := len(arr)
	res := make([]int32, size, size)
	for i, j := size-1, 0; i >= 0; i, j = i-1, j+1 {
		res[j] = arr[i]
	}
	return res
}