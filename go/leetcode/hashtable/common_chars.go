package hashtable

// Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

// You may return the answer in any order.

// Example 1:

// Input: ["bella","label","roller"]
// Output: ["e","l","l"]
// Example 2:

// Input: ["cool","lock","cook"]
// Output: ["c","o"]

// Note:

// 1 <= A.length <= 100
// 1 <= A[i].length <= 100
// A[i][j] is a lowercase letter

func updateGlobal(globalSlice []rune, global, local map[byte]int) {
	for key, val := range global {
		if count, exist := local[key]; exist {
			if count != val {
				delete(global, key)
			}
		} else {
			delete(global, key)
		}
	}
}

func CommonChars(A []string) []string {
	global := make(map[byte]int)
	globalSlice := make([]rune, 0)
	firstEntry := A[0]
	for i := 0; i < len(firstEntry); i++ {
		if _, exist := global[firstEntry[i]]; exist {
			global[firstEntry[i]] = global[firstEntry[i]] + 1
		} else {
			global[firstEntry[i]] = 1
		}
		globalSlice = append(globalSlice, rune(global[firstEntry[i]]))
	}

	for i := 1; i < len(A); i++ {
		arr := A[i]
		size := len(arr)
		local := make(map[byte]int, size)
		for j := 0; j < size; j++ {
			if _, exist := local[arr[j]]; exist {
				local[arr[j]] = local[arr[j]] + 1
			} else {
				local[arr[j]] = 1
			}
		}
		updateGlobal(globalSlice, global, local)
	}

	res := make([]string, 0)
	for key := range global {
		res = append(res, string(key))
	}
	return res
}
