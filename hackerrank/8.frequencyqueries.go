package hackerrank

// FreqQuery implementation
// https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
func FreqQuery(queries [][]int32) []int32 {
	dict := map[int32]int32{}

	res := make([]int32, 0)

	for _, arr := range queries {
		op := arr[0]
		value := arr[1]

		switch op {
		case 1:
			if count, exist := dict[value]; exist {
				dict[value] = count + 1
			} else {
				dict[value] = 1
			}
			break
		case 2:
			if count, exist := dict[value]; exist {
				if count-1 > 0 {
					dict[value] = count - 1
				} else {
					delete(dict, value)
				}
			}
			break
		default:
			found := false
			for _, val := range dict {
				if val == value {
					found = true
					break
				}
			}
			if found {
				res = append(res, 1)
			} else {
				res = append(res, 0)
			}
			break
		}
	}

	return res
}
