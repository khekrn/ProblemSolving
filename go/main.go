package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)
	N, _ := strconv.Atoi(readLine(reader))

	dict := make(map[int]int, N)

	arrTemp := strings.Split(readLine(reader), " ")

	for i := 0; i < len(arrTemp); i++ {
		temp, _ := strconv.Atoi(arrTemp[i])
		if _, exist := dict[temp]; exist {
			dict[temp] = dict[temp] + 1
		} else {
			dict[temp] = 1
		}
	}

	Q, _ := strconv.Atoi(readLine(reader))

	for ; Q > 0; Q-- {
		temp, _ := strconv.Atoi(readLine(reader))

		if _, exist := dict[temp]; exist {
			fmt.Println(dict[temp])
		} else {
			fmt.Println("NOT PRESENT")
		}
	}
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}
