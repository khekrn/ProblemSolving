package main

import (
	"fmt"

	"github.com/khekrn/ps/hackerrank"
)

func main() {
	arr := "UDDDUDUU"
	res := hackerrank.CountingValleys(int32(len(arr)), arr)
	fmt.Println(res)
}
