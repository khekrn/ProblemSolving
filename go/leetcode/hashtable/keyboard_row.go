package hashtable

// Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

// Example:

// Input: ["Hello", "Alaska", "Dad", "Peace"]
// Output: ["Alaska", "Dad"]

// Note:

// You may use one character in the keyboard more than once.
// You may assume the input string will only contain letters of alphabet.

import "strings"

func FindWords(words []string) []string {
	dict := map[rune]int{112: 0, 102: 1, 104: 1, 108: 1, 99: 2, 118: 2, 98: 2, 101: 0, 109: 2, 110: 2, 115: 1, 106: 1, 107: 1, 122: 2, 120: 2, 111: 0, 114: 0, 116: 0, 105: 0, 100: 1, 103: 1, 113: 0, 121: 0, 117: 0, 97: 1, 119: 0}
	res := make([]string, 0)
	for i := 0; i < len(words); i++ {
		lower := []rune(strings.ToLower(words[i]))
		index, _ := dict[rune(lower[0])]
		found := true
		for j := 1; j < len(lower); j++ {
			currentIndex, _ := dict[lower[j]]
			if index != currentIndex {
				found = false
			}
		}
		if found {
			res = append(res, words[i])
		}
	}
	return res
}
