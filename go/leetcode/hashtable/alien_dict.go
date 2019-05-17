package hashtable

func IsAlienSorted(words []string, order string) bool {
	dict := make(map[byte]int, len(order))
	for i := 0; i < len(order); i++ {
		dict[order[i]] = i
	}
	for i, j := 0, 1; j < len(words); i, j = i+1, j+1 {
		if len(words[i]) > len(words[j]) {
			return false
		}
		firstChar, _ := dict[words[i][0]]
		secondChar, _ := dict[words[i][0]]
		if firstChar > secondChar {
			return false
		}
	}
	return true
}
