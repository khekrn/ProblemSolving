package main

import (
	"fmt"

	"github.com/khekrn/ps/others/arrays"
)

func main() {
	arr1 := []int32{-1, 5, 10, 20, 28, 3}
	arr2 := []int32{26, 134, 135, 15, 17}

	fmt.Println(arrays.MinimumDifference(arr1, arr2))
}
