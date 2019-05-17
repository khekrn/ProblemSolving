package hashtable

// We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

// A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

// Return a list of all uncommon words.

// You may return the list in any order.

// Example 1:

// Input: A = "this apple is sweet", B = "this apple is sour"
// Output: ["sweet","sour"]
// Example 2:

// Input: A = "apple apple", B = "banana"
// Output: ["banana"]

// Note:

// 0 <= A.length <= 200
// 0 <= B.length <= 200
// A and B both contain only spaces and lowercase letters.

import "strings"

func exactOnce(dict map[string]int, arr []string) {
	for i := 0; i < len(arr); i++ {
		if _, exist := dict[arr[i]]; exist {
			dict[arr[i]] = dict[arr[i]] + 1
		} else {
			dict[arr[i]] = 1
		}
	}
}

func UncommonFromSentences(A string, B string) []string {
	dict := make(map[string]int)

	arr1 := strings.Split(A, " ")
	exactOnce(dict, arr1)

	arr2 := strings.Split(B, " ")
	exactOnce(dict, arr2)

	res := make([]string, 0)

	for key, value := range dict {
		if value == 1 {
			res = append(res, key)
		}
	}
	return res
}
