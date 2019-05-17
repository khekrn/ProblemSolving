package search

import (
	"fmt"
	"sort"
)

func Solve(array []int, target int, N int) int {
	left := 0
	right := len(array) - 1
	if target >= array[right] {
		return right
	}
	for left <= right {
		mid := left + (right-left)/2
		if array[mid] == target {
			return mid
		}
		if array[mid] <= target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return 0
}

func checkDuplicates(array []int, index int, value int) int {
	temp := index
	for i := index + 1; i < len(array); i++ {
		if value != array[i] {
			return temp
		}
		temp = i
	}
	return index
}

func main() {

	var N int //total number of soldiers
	fmt.Scan(&N)

	powers := make([]int, N) // power of each soldier
	for i := 0; i < N; i++ {
		fmt.Scan(&powers[i])
	}
	sort.Ints(powers)
	sumPower := make([]int, N)
	sumPower[0] = powers[0]
	for i := 1; i < N; i++ {
		sumPower[i] = sumPower[i-1] + powers[i]

	}
	var Q int          //total number of rounds
	var bishuPower int // bishu's power (varies each round)
	fmt.Scan(&Q)

	for ; 0 < Q; Q-- {
		fmt.Scan(&bishuPower)
		index := search(powers, bishuPower, N)
		correctIndex := checkDuplicates(powers, index, powers[index])
		fmt.Println(correctIndex+1, sumPower[correctIndex])
	}

}
