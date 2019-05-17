package hashtable

import "fmt"

func FirstUniqChar(s string) int {
	arr := make([]int, len(s), len(s))
	dict := make(map[int32]int)
	for index, val := range s {
		if mapIndex, exist := dict[val]; !exist {
			arr[index] = 1
			dict[val] = index
		} else {
			arr[mapIndex]++
		}
	}

	for index, val := range arr {
		if val == 1 {
			return index
		}
	}
	return -1
}

func FirstUniqCharV2(s string) int {
	if len(s) == 0 {
		return -1
	}
	result := make([]int, 26)
	for _, value := range s {
		result[value-'a'] += 1
	}

	fmt.Println(result)

	for index, value := range s {
		if result[value-'a'] == 1 {
			return index
		}
	}

	return -1
}
