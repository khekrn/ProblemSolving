package array

func matchingStrings(strings []string, queries []string) []int32 {
	res := make([]int32, len(queries))
	dict := make(map[string]int32, 0)

	for _, value := range strings {
		if _, ok := dict[value]; ok {
			dict[value] = dict[value] + 1
		} else {
			dict[value] = 1
		}
	}
	for index, q := range queries {
		if count, ok := dict[q]; ok {
			res[index] = count
		} else {
			res[index] = 0
		}
	}

	return res
}
