package hashtable

// Given two strings s and t which consist of only lowercase letters.

// String t is generated by random shuffling string s and then add one more letter at a random position.

// Find the letter that was added in t.

// Example:

// Input:
// s = "abcd"
// t = "abcde"

// Output:
// e

// Explanation:
// 'e' is the letter that was added.

func FindTheDifference(s string, t string) byte {
    dict := make(map[int32]int)
    for _, val := range s {
		dict[val] = dict[val]+1
	}
	
	for _, val := range t {
		dict[val] = dict[val] - 1
		if dict[val] == -1 {
			return byte(val)
		}
	}
    return 0
}