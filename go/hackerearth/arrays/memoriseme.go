package arrays

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Solve() {

	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	sep := strings.Split(scanner.Text(), " ")

	dict := make(map[int]int, N)

	for _, item := range sep {
		temp, _ := strconv.Atoi(item)
		if _, exist := dict[temp]; exist {
			dict[temp] = dict[temp] + 1
		} else {
			dict[temp] = 1
		}
	}

	scanner.Scan()
	Q, _ := strconv.Atoi(scanner.Text())
	for i := 0; i < Q; i++ {
		scanner.Scan()
		temp, _ := strconv.Atoi(scanner.Text())
		if _, exist := dict[temp]; exist {
			fmt.Println(dict[temp])
		} else {
			fmt.Println("NOT PRESENT")
		}
	}
}
