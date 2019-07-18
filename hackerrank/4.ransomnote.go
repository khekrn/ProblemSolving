package hackerrank

import "fmt"

// CheckMagazine implementation
func CheckMagazine(magazine []string, note []string) {

	dict := map[string]int{}

	res := "Yes"

	for _, key := range magazine {
		if _, ok := dict[key]; ok {
			dict[key] = dict[key] + 1
		} else {
			dict[key] = 1
		}
	}

	for _, item := range note {
		if magazineItem, ok := dict[item]; ok {
			newValue := magazineItem - 1
			if newValue < 0 {
				res = "No"
				break
			}
			dict[item] = newValue

		} else {
			res = "No"
			break
		}
	}

	fmt.Println(res)
}
