package main

import (
	"fmt"

	"github.com/khekrn/ps/hackerrank"
)

func main() {
	q := [][]int32{{1, 1}, {2, 2}, {3, 2}, {1, 1}, {1, 1}, {2, 1}, {3, 2}}
	res := hackerrank.FreqQuery(q)
	fmt.Println(res)
}
